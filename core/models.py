from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome_pessoa = models.CharField(max_length=100)
    
def __str__(self):
    return self.nome_pessoa
