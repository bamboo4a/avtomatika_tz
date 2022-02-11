from django.urls import path

from shops.api_views import UserShopList, VisitShopApiView

urlpatterns = [
    path("<str:phone_number>/list/", UserShopList.as_view(), name="users_shop_list"),
    path("<str:phone_number>/visit/", VisitShopApiView.as_view(), name="users_shop_visit"),
]
