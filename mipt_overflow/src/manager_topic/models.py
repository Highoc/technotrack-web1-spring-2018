# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from manager_category.models import Category

class Topic(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='topics',
        verbose_name='Автор топика'
    )

    text = models.TextField(
        max_length=40980,
        verbose_name='Текст топика'
    )

    categories = models.ManyToManyField(
        Category,
        related_name='topics',
        verbose_name='Категория'
    )

    name = models.CharField(
        max_length=127,
        verbose_name='Название топика'
    )

    is_archive = models.BooleanField(
        default=False,
        verbose_name='В архиве?'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Топик'
        verbose_name_plural = 'Топики'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name