from django.db import models

from users.models import User


class Shop(models.Model):
    name = models.CharField(verbose_name="Торговая точка", max_length=255)
    user = models.ForeignKey(User, verbose_name="Работник", related_name="shops", on_delete=models.CASCADE)


class ShopVisit(models.Model):
    time_visit = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(verbose_name="Координаты: широта", max_digits=6, decimal_places=4)
    longitude = models.DecimalField(verbose_name="Координаты: долгота", max_digits=6, decimal_places=4)
    user = models.ForeignKey(
        User,
        verbose_name="Работник",
        related_name="shop_visits",
        on_delete=models.CASCADE,
        null=True
    )
    shop = models.ForeignKey(
        Shop,
        verbose_name="Торговая точка",
        related_name="shop_visits",
        on_delete=models.CASCADE,
        null=True
    )
