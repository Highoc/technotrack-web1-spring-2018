# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from manager_topic.models import Topic

class Comment(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='autor_comments',
        verbose_name='Author name'
    )

    topic = models.ForeignKey(
        Topic,
        related_name='topic_comments',
        verbose_name='Topic'
    )

    text = models.TextField(
        max_length=2047,
        verbose_name='Comment text'
    )

    comment = models.ForeignKey(
        'self', blank=True, null=True,
        related_name='child_comments',
        verbose_name='Parent comment'
    )

    is_archive = models.BooleanField(
        default=False,
        verbose_name='Comment is archived'
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
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = 'topic', 'author', 'id'

    def __unicode__(self):
        return str(self.id)

