from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    bio = models.TextField("Descrição", default="sem bio...")
    avatar = models.ImageField("Imagem de perfil", upload_to='avatars', default='icon.png')
    created = models.DateTimeField("Data de criação", auto_now_add=True)
    altered = models.DateTimeField("Data de atualização", auto_now=True)

    def __str__(self):
        return f"Perfil do {self.user.username}"

