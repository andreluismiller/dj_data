from django.urls import path
from .views import (
    home_view,
    PostListView,
    PostDetailView,
)

app_name = 'posts_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('posts/', PostListView.as_view(), name='lista'),
    path('posts/<slug:pk>', PostDetailView.as_view(), name='detalhes')
]