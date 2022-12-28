from django.db import models

class PostInfo(models.Model):
    REDE = (
        ('IG', 'Instagram'),
        ('FB', 'Facebook'),
        ('TK', 'Tiktok'),
        ('YT', 'Youtube'),
    )
    FORMATO = (
        ('ES', 'Estático'),
        ('CR', 'Carrossel'),
        ('VD', 'Reel/Video'),
        ('SH', 'Youtube Shorts'),
    )
    id_post = models.CharField(blank=False, max_length=30, primary_key=True, verbose_name="Id do post")
    plataform = models.CharField(blank = False, max_length=2, choices=REDE, verbose_name="Rede social")
    type_post = models.CharField(blank = False, max_length=2, choices=FORMATO, verbose_name="Formato do post")
    link = models.URLField(blank = False, max_length=200, verbose_name="Link do post")
    data_post = models.DateField(blank = False, auto_now=False, auto_now_add=False, verbose_name="Data de postagem")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de cadastro do post no sistema")

    def __str__(self):
        pass

