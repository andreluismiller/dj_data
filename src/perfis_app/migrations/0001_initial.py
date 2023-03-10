# Generated by Django 4.1.4 on 2022-12-28 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='sem bio...', verbose_name='Descrição')),
                ('avatar', models.ImageField(default='icon.png', upload_to='avatars', verbose_name='Imagem de perfil')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('altered', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
