# Generated by Django 4.0.4 on 2022-05-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_page_numero_casa_alter_page_porcentaje_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True, verbose_name='Comentarios'),
        ),
        migrations.AlterField(
            model_name='page',
            name='porcentaje_casa',
            field=models.FloatField(verbose_name='Porcentaje %'),
        ),
    ]