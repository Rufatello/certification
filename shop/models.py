from django.conf import settings
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    price = models.PositiveSmallIntegerField(verbose_name='Цена')
    model = models.CharField(verbose_name='Модель', max_length=70)
    data = models.DateField(verbose_name='Дата_выхода')


class Factory(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название завода')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Контакты', on_delete=models.CASCADE)


