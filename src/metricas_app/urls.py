from django.urls import path
from .views import index, PostListView, PostDetailView, PostInput, PostMetricsInput


urlpatterns = [
    #path('', index, name='index'),
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='detalhes-post'),
    path('cadastrar/', PostInput, name='cadastrar-post'),
    path('cadastrar/metricas/', PostMetricsInput, name='cadastrar-metricas'),
]