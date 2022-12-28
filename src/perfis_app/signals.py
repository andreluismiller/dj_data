"""
Signals é uma espécie de sistema de comunicação entre as aplicações Django
Baseado em uma notificação enviada pelo emissor, o receptor performa determinada ação
Neste caso, o usuário (emissor) informará o perfil (receptor) que uma instância do usuário foi criada, 
e portanto, um perfir deverá ser criado para esse usuário
"""

from .models import Perfil
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def post_save_criar_perfil(sender, instance, created, **kwargs):
    print(sender)
    print(instance)
    print(created)
    if created:
        Perfil.objects.create(user=instance)