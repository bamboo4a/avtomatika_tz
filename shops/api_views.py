from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404
from rest_framework import serializers
from shops.models import Shop, ShopVisit
from shops.serializers import UserShopSerializer, VisitShopCreateSerializer, VisitShopDetailSerializer
from rest_framework import status
from rest_framework.response import Response

from users.models import User


class UserShopList(ListAPIView):
    permission_classes = []
    serializer_class = UserShopSerializer

    def get_queryset(self):
        phone_number = self.kwargs.get("phone_number")
        response_query = Shop.objects.filter(user__phone_number=phone_number)
        if not response_query:
            raise serializers.ValidationError({"not found": phone_number})
        return response_query


class VisitShopApiView(CreateAPIView):
    permission_classes = []
    serializer_class = VisitShopCreateSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        phone_number = self.kwargs.get("phone_number")
        ctx.update(
            {
                "phone_number": phone_number,
                "user": get_object_or_404(User, phone_number=phone_number)
            }
        )
        return ctx

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_visit = ShopVisit.objects.create(**serializer.data)
        response = VisitShopDetailSerializer(new_visit).data
        return Response(response, status=status.HTTP_201_CREATED)
