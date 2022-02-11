from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name="Имя работника", max_length=255)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=255, unique=True)
