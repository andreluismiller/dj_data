from django.db import models
from perfis_app.models import Perfil


# Classe para cadastro do post
class PostInfo(models.Model):
    SOCIAL_NET = (
        ('IG', 'Instagram'),
        ('FB', 'Facebook'),
        ('TK', 'Tiktok'),
        ('YT', 'Youtube'),
    )
    FORMAT = (
        ('ES', 'Estático'),
        ('CR', 'Carrossel'),
        ('VD', 'Reel/Video'),
        ('SH', 'Youtube Shorts'),
    )
    id_post = models.CharField(blank=False, max_length=30, primary_key=True, verbose_name="Id do post")
    plataform = models.CharField(blank = False, max_length=2, choices=SOCIAL_NET, verbose_name="Rede social")
    post_type = models.CharField(blank = False, max_length=2, choices=FORMAT, verbose_name="Formato do post")
    post_link = models.URLField(blank = False, max_length=200, verbose_name="Link do post")
    post_date = models.DateField(blank = False, auto_now=False, auto_now_add=False, verbose_name="Data de postagem")
    user_responsable = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Usuário")
    date_input = models.DateTimeField(auto_now_add=True, verbose_name="Data de cadastro do post no sistema")


    # Salvando os objetos criados
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    # Método de exibição dos dados
    def __str__(self):
        return f"Post ID: {self.id_post}"

