# Generated by Django 3.2.7 on 2021-10-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prato', '0002_pratopedido'),
        ('pedido', '0003_auto_20211013_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='pratos',
            field=models.ManyToManyField(to='prato.PratoPedido'),
        ),
    ]
