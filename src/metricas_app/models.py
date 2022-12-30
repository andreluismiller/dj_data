from django.db import models
from django.urls import reverse
import uuid
from perfis_app.models import Perfil


class Post(models.Model):
    """Modelo que representa as informações básicas de um post (mas não suas métricas)"""
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

    def __str__(self):
        """String de representação do objeto do modelo"""
        return f"Link do post: {self.post_link}"

    def get_absolute_url(self):
        """Retorna a url para acessar os detalges do post"""
        return reverse('detalhes-post', args=[str(self.id_post)])



class PostInstance(models.Model):
    """Modelo que representa as diferentes instâncias (métricas por data) de determinado post"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único do post')
    post = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True)
    date_collect = models.DateField(blank = False, auto_now=False, auto_now_add=False, verbose_name="Data de referência das métricas")
    reach = models.IntegerField(blank = False, verbose_name="Quantidade de alcance ou impressões")
    likes = models.IntegerField(blank = False, verbose_name="Quantidade de likes")
    comments = models.IntegerField(blank = False, verbose_name="Quantidade de comentários")
    shares = models.IntegerField(blank = True, verbose_name="Quantidade de compartilhamentos")
    saves = models.IntegerField(blank = True, verbose_name="Quantidade de salvos")
    views = models.IntegerField(blank = True, verbose_name="Quantidade de visualizações")
    Engajement = models.IntegerField(blank=True, verbose_name="Engajamento", null=True)
    date_insert = models.DateTimeField(auto_now_add=True, verbose_name="Data de inserção dos dados no sistema")
    user_input = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Usuário")

    class Meta:
        """Classe para ditar a ordem dos registros retornados"""
        ordering = ['post', 'date_collect']

    def __str__(self):
        """String de representação do objeto do modelo"""
        return f"Post Id: {self.post.id_post}, Rede: {self.post.plataform}, Tipo de post: {self.post.post_type}, Data de coleta das métricas: {self.date_collect.strftime('%d/%m/%Y')}, Alcance: {self.reach}, Likes: {self.likes}, Comentários: {self.comments}"








# class DailyMetrics(models.Model):
#     post = models.ForeignKey(PostInfo, on_delete=models.CASCADE) 
#     date_collect = models.DateField(blank = False, auto_now=False, auto_now_add=False, verbose_name="Data de referência das métricas")
#     reach = models.IntegerField(blank = False, verbose_name="Quantidade de alcance ou impressões")
#     likes = models.IntegerField(blank = False, verbose_name="Quantidade de likes")
#     comments = models.IntegerField(blank = False, verbose_name="Quantidade de comentários")
#     shares = models.IntegerField(blank = True, verbose_name="Quantidade de compartilhamentos")
#     saves = models.IntegerField(blank = True, verbose_name="Quantidade de salvos")
#     views = models.IntegerField(blank = True, verbose_name="Quantidade de visualizações")
#     Engajement = models.IntegerField(blank=True, verbose_name="Engajamento")
#     date_insert = models.DateTimeField(auto_now_add=True, verbose_name="Data de inserção dos dados no sistema")
#     user_input = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Usuário")


#     #Método para salvar as métricas
#     def save(self, *args, **kwargs):
#         # Cãlculo do engajamento (likes e comments)
#         self.Engajement = self.likes + self.comments
#         return super().save(*args, **kwargs)

#     # Método de exibição dos dados
#     def __str__(self):
#         return f"Post Id: {self.post.id_post}, Rede: {self.post.plataform}, Tipo de post: {self.post.post_type}, Data de coleta das métricas: {self.date_collect.strftime('%d/%m/%Y')}, Alcance: {self.reach}, Likes: {self.likes}, Comentários: {self.comments}"