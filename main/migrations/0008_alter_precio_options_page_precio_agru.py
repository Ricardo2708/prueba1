# Generated by Django 4.0.4 on 2022-05-23 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_precio_precio_agru24_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='precio',
            options={'verbose_name': 'Precio De Agrupacion', 'verbose_name_plural': 'Precios De Agrupaciones'},
        ),
        migrations.AddField(
            model_name='page',
            name='precio_agru',
            field=models.IntegerField(default=1, verbose_name='Precio De La Agrupacion'),
            preserve_default=False,
        ),
    ]