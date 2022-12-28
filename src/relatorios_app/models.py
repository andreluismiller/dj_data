from django.db import models
from perfis_app.models import Perfil

class Relatorio(models.Model):
    nome = models.CharField(max_length=120)
    imagem = models.ImageField(upload_to='relatorios', blank=True)
    insights = models.TextField()
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    created = models.DateTimeField("Data de criação", auto_now_add=True)
    updated = models.DateTimeField("Data de atualização", auto_now=True)


    def __str__(self):
        return str(self.nome)