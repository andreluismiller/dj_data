from django.db import models
from posts_app.models import PostInfo
from perfis_app.models import Perfil

# Classe para cadastro das métricas
# Um mesmo post pode ter n linhas de métricas, uma para cada data
class DailyMetrics(models.Model):
    post = models.ForeignKey(PostInfo, on_delete=models.CASCADE)
    # !!!! Necessário criar PK como combinação do id (index) e data!!!!    
    date_collect = models.DateField(blank = False, auto_now=False, auto_now_add=False, verbose_name="Data de referência das métricas")
    reach = models.IntegerField(blank = False, verbose_name="Quantidade de alcance ou impressões")
    likes = models.IntegerField(blank = False, verbose_name="Quantidade de likes")
    comments = models.IntegerField(blank = False, verbose_name="Quantidade de comentários")
    shares = models.IntegerField(blank = True, verbose_name="Quantidade de compartilhamentos")
    saves = models.IntegerField(blank = True, verbose_name="Quantidade de salvos")
    views = models.IntegerField(blank = True, verbose_name="Quantidade de visualizações")
    Engajement = models.IntegerField(blank=True, verbose_name="Engajamento")
    date_insert = models.DateTimeField(auto_now_add=True, verbose_name="Data de inserção dos dados no sistema")
    user_input = models.ForeignKey(Perfil, on_delete=models.CASCADE, verbose_name="Usuário")


    #Método para salvar as métricas
    def save(self, *args, **kwargs):
        # Cãlculo do engajamento (likes e comments)
        self.Engajement = self.likes + self.comments
        return super().save(*args, **kwargs)

    # Método de exibição dos dados
    def __str__(self):
        return f"Post Id: {self.post.id_post}, Rede: {self.post.plataform}, Tipo de post: {self.post.post_type}, Data de coleta das métricas: {self.date_collect.strftime('%d/%m/%Y')}, Alcance: {self.reach}, Likes: {self.likes}, Comentários: {self.comments}"