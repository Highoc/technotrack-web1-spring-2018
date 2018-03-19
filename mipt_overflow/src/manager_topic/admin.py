# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Topic

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = 'name', 'author', 'created', 'updated'
    search_fields = 'name', 'author__username'
    list_filter = 'is_archive',