# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-25 16:26
from __future__ import unicode_literals

import aprendizaje.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Nombre de la lecci\xf3n')),
                ('contenido', models.TextField(verbose_name='Contenido de la lecci\xf3n')),
                ('order', aprendizaje.fields.OrderField(blank=True)),
                ('url_video', models.FileField(blank=True, null=True, upload_to=b'')),
                ('nombre_video', models.CharField(blank=True, max_length=250, null=True, verbose_name='Nombre del video')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Lecci\xf3n',
                'verbose_name_plural': 'Lecciones',
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Nombre del curso')),
                ('slug', models.SlugField(editable=False, max_length=250, unique=True)),
                ('imagen', models.FileField(blank=True, null=True, upload_to='images')),
                ('imagen_banner', models.FileField(blank=True, null=True, upload_to='banner')),
                ('descripcion', models.TextField(verbose_name='Descripci\xf3n del curso')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('activo', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-fecha',),
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Modulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250, verbose_name='Nombre del tema')),
                ('order', aprendizaje.fields.OrderField(blank=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='aprendizaje.Cursos')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.AddField(
            model_name='contenidos',
            name='modulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contenidos', to='aprendizaje.Modulos'),
        ),
    ]
