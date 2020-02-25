# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from .fields import OrderField
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class Cursos(models.Model):
    titulo = models.CharField('Nombre del curso', max_length=250)
    slug = models.SlugField(max_length=250, unique=True, editable=False)
    imagen = models.FileField(upload_to='images', null=True, blank=True)
    imagen_banner = models.FileField(upload_to='banner', null=True, blank=True)
    descripcion = models.TextField('Descripción del curso')
    fecha = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=False)
    # usuarios_siguiendo = models.ManyToManyField(User,blank=True,editable=False)

    class Meta:
        ordering = ('-fecha',)
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.slug = (slugify(self.titulo))
        super(Cursos, self).save(*args, **kwargs)

@python_2_unicode_compatible
class Modulos(models.Model):
    curso = models.ForeignKey(Cursos, related_name='modules',on_delete=models.CASCADE)
    titulo = models.CharField('Nombre del tema', max_length=250)
    order = OrderField(blank=True, for_fields=['curso'])

    class Meta:
        ordering = ['order']
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return '{0}. {1}'.format(self.order, self.titulo)

@python_2_unicode_compatible
class Contenidos(models.Model):
    modulo = models.ForeignKey(Modulos, related_name='contenidos',on_delete=models.CASCADE)
    titulo = models.CharField('Nombre de la lección', max_length=250)
    contenido = models.TextField('Contenido de la lección')
    order = OrderField(blank=True, for_fields=['modulo'])
    url_video = models.FileField(null = True, blank = True)
    nombre_video = models.CharField('Nombre del video', max_length=250,
                                    null=True, blank=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Lección'
        verbose_name_plural = 'Lecciones'

    def __str__(self):
        return self.modulo.titulo

