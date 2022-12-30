# Generated by Django 4.1.4 on 2022-12-29 04:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('perfis_app', '0001_initial'),
        ('metricas_app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Id do post')),
                ('plataform', models.CharField(choices=[('IG', 'Instagram'), ('FB', 'Facebook'), ('TK', 'Tiktok'), ('YT', 'Youtube')], max_length=2, verbose_name='Rede social')),
                ('post_type', models.CharField(choices=[('ES', 'Estático'), ('CR', 'Carrossel'), ('VD', 'Reel/Video'), ('SH', 'Youtube Shorts')], max_length=2, verbose_name='Formato do post')),
                ('post_link', models.URLField(verbose_name='Link do post')),
                ('post_date', models.DateField(verbose_name='Data de postagem')),
                ('date_input', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro do post no sistema')),
                ('user_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfis_app.perfil', verbose_name='Usuário')),
            ],
        ),
        migrations.CreateModel(
            name='PostInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único do post', primary_key=True, serialize=False)),
                ('date_collect', models.DateField(verbose_name='Data de referência das métricas')),
                ('reach', models.IntegerField(verbose_name='Quantidade de alcance ou impressões')),
                ('likes', models.IntegerField(verbose_name='Quantidade de likes')),
                ('comments', models.IntegerField(verbose_name='Quantidade de comentários')),
                ('shares', models.IntegerField(blank=True, verbose_name='Quantidade de compartilhamentos')),
                ('saves', models.IntegerField(blank=True, verbose_name='Quantidade de salvos')),
                ('views', models.IntegerField(blank=True, verbose_name='Quantidade de visualizações')),
                ('Engajement', models.IntegerField(blank=True, verbose_name='Engajamento')),
                ('date_insert', models.DateTimeField(auto_now_add=True, verbose_name='Data de inserção dos dados no sistema')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='metricas_app.post')),
                ('user_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perfis_app.perfil', verbose_name='Usuário')),
            ],
            options={
                'ordering': ['post', 'date_collect'],
            },
        ),
        migrations.DeleteModel(
            name='DailyMetrics',
        ),
    ]