from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)  # Autoincrementável, não precisa de valor padrão
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.IntegerField()
    foto = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def __str__(self):
        return self.nome















"""""
from django.db import models

# Create your models here.

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)  # Nome do produto
    foto = models.ImageField(upload_to='produtos/')  # Foto do produto
    descricao = models.TextField()  # Descrição do produto
    quantidade = models.IntegerField()  # Quantidade do produto
    """
