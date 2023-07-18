from django.db import models

# Create your models here.


class Carro(models.Model):

    marca = models.CharField(max_length=255)
    ano = models.IntegerField()
    cor = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)

    def __str__(self):
        return self.modelo
    