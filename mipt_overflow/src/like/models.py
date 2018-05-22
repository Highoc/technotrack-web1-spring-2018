# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from manager_topic.models import Topic
# Create your models here.

class Like(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='autor_likes',
        verbose_name='Автор'
    )

    topic = models.ForeignKey(
        Topic,
        related_name='topic_likes',
        verbose_name='Топик'
    )

    is_archive = models.BooleanField(
        default=False,
        verbose_name='Лайк удален?'
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
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        ordering = 'topic', 'author', 'id'

    def __unicode__(self):
        return str(self.id)

