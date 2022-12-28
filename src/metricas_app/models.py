from django.db import models
from posts_app.models import PostInfo


class DailyMetrics(models.Model):
    post = models.ForeignKey(PostInfo, on_delete=models.CASCADE)    
    data_collect = models.DateField(blank = False, auto_now=False, auto_now_add=False, verbose_name="Data de referência das métricas")
    reach = models.IntegerField(blank = False, verbose_name="Quantidade de alcance ou impressões")
    likes = models.IntegerField(blank = False, verbose_name="Quantidade de likes")
    comments = models.IntegerField(blank = False, verbose_name="Quantidade de comentários")
    shares = models.IntegerField(blank = True, verbose_name="Quantidade de compartilhamentos")
    saves = models.IntegerField(blank = True, verbose_name="Quantidade de salvos")
    views = models.IntegerField(blank = True, verbose_name="Quantidade de visualizações")
    data_insert = models.DateTimeField(auto_now_add=True, verbose_name="Data de inserção dos dados no sistema")

    def __str__(self):
        pass