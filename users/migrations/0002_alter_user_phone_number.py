# Generated by Django 4.0.2 on 2022-02-11 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=255, unique=True, verbose_name='Номер телефона'),
        ),
    ]
