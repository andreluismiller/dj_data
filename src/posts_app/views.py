from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostInfo


# Função para carregar home
def home_view(request):
    return render(request, 'posts_app/home.html', {})


# Classe para exibir a lista de posts
# Também é possível criar função a partir da classe para usar na URL e templates
class PostListView(ListView):
    model = PostInfo
    template_name = 'posts_app/main.html'


# Classe para exibir detalhes dos posts
class PostDetailView(DetailView):
    model = PostInfo
    template_name = 'posts_app/detail.html'
