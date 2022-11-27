# Generated by Django 3.2.7 on 2021-09-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
