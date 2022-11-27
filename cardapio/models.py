from django.db import models
from prato.models import Prato

class Cardapio(models.Model):
    nome = models.CharField(max_length=100)
    pratos = models.ManyToManyField(Prato)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome




