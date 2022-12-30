
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from metricas_app.views import HomePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage, name='home'),
    path('post/', include('metricas_app.urls')),
    #path('', include('posts_app.urls', namespace='posts_app')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)