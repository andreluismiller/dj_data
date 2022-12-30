from django import forms
from django.forms import ModelForm
from .models import Post, PostInstance


class CadastrarPostForm(ModelForm):
    """Classe para cadastro de post"""
    class Meta:
        model = Post
        fields = ['id_post', 'plataform', 'post_type', 'post_link', 'post_date']



class CadastrarMetricasForm(ModelForm):
    """Classe para cadastro das métricas do post"""
    class Meta:
        model = PostInstance
        exclude = ['id', 'date_insert', 'Engajement', 'user_input']
        