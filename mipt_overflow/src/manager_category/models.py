# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):

    name = models.CharField(
        max_length=127,
        verbose_name='Category name'
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
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name

