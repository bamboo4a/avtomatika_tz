from django.contrib import admin
from django.contrib.admin import ModelAdmin
from shops.models import Shop, ShopVisit


@admin.register(Shop)
class ShopAdmin(ModelAdmin):
    search_fields = ["name"]


@admin.register(ShopVisit)
class ShopVisitAdmin(ModelAdmin):
    search_fields = ["user__name", "shop__name"]

