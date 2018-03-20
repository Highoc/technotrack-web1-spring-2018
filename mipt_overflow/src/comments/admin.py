# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class TopicAdmin(admin.ModelAdmin):
    list_display = 'id', 'topic', 'author', 'text', 'comment', 'created', 'updated'
    search_fields = 'topic__name', 'author__username'
    list_filter = ['is_archive']
