from django.urls import path, include


app_name = "api_user_shop"

urlpatterns = [
    path("", include("shops.api_urls.user_shop")),
]
