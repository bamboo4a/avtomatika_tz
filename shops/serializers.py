from rest_framework import serializers
from shops.models import Shop, ShopVisit


class UserShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ["id", "name"]
        read_only_fields = fields


class VisitShopCreateSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all(), write_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    shop_id = serializers.PrimaryKeyRelatedField(read_only=True)
    latitude = serializers.DecimalField(max_digits=6, decimal_places=4)
    longitude = serializers.DecimalField(max_digits=6, decimal_places=4)

    class Meta:
        model = Shop
        fields = ["id", "latitude", "longitude", "user_id", "shop_id"]
        read_only_fields = fields

    def validate(self, attrs):
        shop = attrs.get("id")
        phone_number = self.context.get("phone_number")
        if not Shop.objects.filter(id=shop.id, user__phone_number=phone_number).exists():
            raise serializers.ValidationError({"not_found": "user_not_found"})
        # append user and shop
        attrs["user_id"] = self.context.get("user")
        attrs["shop_id"] = shop
        return attrs


class VisitShopDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopVisit
        fields = ["id", "time_visit"]
