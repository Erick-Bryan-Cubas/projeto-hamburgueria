# core/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # Descrição não obrigatória
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    preparation_time = models.IntegerField(default=5)  # Campo para tempo de preparo em minutos com valor padrão
    discount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Campo para desconto percentual

    def __str__(self):
        return str(self.name)
