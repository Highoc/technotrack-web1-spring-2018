# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Topic

def topic_list(request):
    context = {
        'topics': Topic.objects.all().filter(is_archive=False)
    }
    return render(request, 'manager_topic/list.html', context)

def topic_add(request):
    return render(request, 'manager_topic/add.html')

def topic_detail(request, pk=None):
    topic = Topic.objects.get(id=pk)
    context = {
        'topic': topic,
        'comments': topic.topic_comments.all().filter(is_archive=False).filter(comment=None)
    }
    return render(request, 'manager_topic/detail.html', context)

def topic_remove(request, pk=None):
    context = {
        'topic': Topic.objects.get(id=pk)
    }
    return render(request, 'manager_topic/remove.html', context)

def topic_statistics(request, pk=None):
    context = {
        'topic': Topic.objects.get(id=pk)
    }
    return render(request, 'manager_topic/statistics.html', context)
