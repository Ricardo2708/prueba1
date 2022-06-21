# Generated by Django 4.0.4 on 2022-05-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_page_fecha_generica'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmobiliaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_inmo', models.CharField(max_length=50, unique=True, verbose_name='Nombre de La Inmobiliaria')),
                ('pertenecia_inmo', models.CharField(max_length=50, unique=True, verbose_name='Proyecto Al Que Pertenece')),
                ('estado_proyecto', models.BooleanField(verbose_name='Estado Del Proyecto')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado El ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado El ')),
            ],
            options={
                'verbose_name': 'Inmobiliaria',
                'verbose_name_plural': 'Inmobiliaria',
            },
        ),
    ]