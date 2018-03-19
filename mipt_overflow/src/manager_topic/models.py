# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from manager_category.models import Category

class Topic(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='topics',
        verbose_name='Author name'
    )

    categories = models.ManyToManyField(
        Category,
        related_name='topics',
        verbose_name='Category'
    )

    name = models.CharField(
        max_length=127,
        verbose_name='Topic name'
    )

    is_archive = models.BooleanField(
        default=False,
        verbose_name='Topic is archived'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation date'
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Updation date'
    )

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name