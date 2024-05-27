from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    sobrenome = models.Field(max_length=100)
    data = models.DateField()
    fone = models.CharField(max_length=20)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)