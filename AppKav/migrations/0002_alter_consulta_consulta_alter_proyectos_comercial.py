# Generated by Django 5.0.3 on 2024-03-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppKav', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='consulta',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='comercial',
            field=models.CharField(max_length=60),
        ),
    ]