from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, PostInstance
from .forms import CadastrarPostForm, CadastrarMetricasForm


def HomePage(request):
    return render(request, 'landing.html')


def index(request):
    """"Função view para a homepage do site"""

    # Contagem dos posts cadastrados
    num_posts = Post.objects.all().count()
    # Contagem das instâncias cadastradas
    num_posts_instances = PostInstance.objects.all().count()
    # Contagem de visitas (sessões) à view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_posts': num_posts,
        'num_posts_instances': num_posts_instances,
        'num_visits': num_visits,
    }

    return render(request, 'metricas_app/index.html', context=context)


class PostListView(generic.ListView):
    """Classe para exibição dos detalhes dos posts"""
    model = Post
    template_name = 'metricas_app/post_list'



class PostDetailView(generic.DetailView):
    """Classe para exibição dos detalhes do post"""
    model = Post
    template_name = 'metricas_app/post_detalhes.html'


def PostInput(request):
    """Função para o usuário realizar o cadastro de post via form"""    
    #Verificando o tipo de requisição feita
    form_post = CadastrarPostForm()
    if request.method == 'POST':
        print("Recebendo uma requisição POST")
        form_post = CadastrarPostForm(request.POST)
        #Verificando se o formulário é válido
        if form_post.is_valid():
            print("O formulário é válido")
            print(form_post.cleaned_data)
            # Obtenção dos dados inseridos no formulário
            id_post = form_post.cleaned_data['id_post']
            plataform = form_post.cleaned_data['plataform']
            post_type = form_post.cleaned_data['post_type']
            post_link = form_post.cleaned_data['post_link']
            post_date = form_post.cleaned_data['post_date']
            # Salvar os inputs do formulário no banco de dados
            Post.objects.create(
                id_post = id_post, 
                plataform = plataform,
                post_type = post_type,
                post_link = post_link,
                post_date = post_date
            )
            print("O post foi cadastrado!")
            # Retornar o usuário para página com listagem dos posts
            return redirect('/posts') 
    context = {
        'form_post': form_post
    }
    return render(request, 'metricas_app/post_input.html', context=context)


def PostMetricsInput(request):
    """Função para cadastro de métricas diárias do post"""
    form_metrics = CadastrarMetricasForm()
    if request.method == 'POST':
        print("Recebendo uma requisição POST")
        form_metrics = CadastrarMetricasForm(request.POST)
        if form_metrics.is_valid():
            print("O formulário é válido")
            print(form_metrics.cleaned_data)
            post = form_metrics.cleaned_data['post']
            date_collect = form_metrics.cleaned_data['date_collect']
            reach = form_metrics.cleaned_data['reach']
            likes = form_metrics.cleaned_data['likes']
            comments = form_metrics.cleaned_data['comments']
            shares = form_metrics.cleaned_data['shares']
            saves = form_metrics.cleaned_data['saves']
            views = form_metrics.cleaned_data['views']
            PostInstance.objects.create(
                post = post,
                date_collect = date_collect,
                reach = reach,
                likes = likes,
                comments = comments,
                shares = shares,
                saves = saves,
                views = views
            )
            print("As métricas do post foram cadastradas!")
    context = {
        'form_metrics': form_metrics
    }
    return render(request, 'metricas_app/metrics_input.html', context=context)

