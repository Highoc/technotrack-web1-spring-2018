# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def topic_list(request):
    return render(request, 'manager_topic/list.html')

def topic_add(request):
    return render(request, 'manager_topic/add.html')

def topic_detail(request, pk=None):
    context = {}
    context['topic'] = {
        'name': 'Topic #{}'.format(pk),
        'id': pk,
    }
    return render(request, 'manager_topic/detail.html', context)

def topic_remove(request, pk=None):
    context = {}
    context['topic'] = {
        'name': 'Topic #{}'.format(pk),
        'id': pk,
    }
    return render(request, 'manager_topic/remove.html', context)

def topic_statistics(request, pk=None):
    context = {}
    context['topic'] = {
        'name': 'Topic #{}'.format(pk),
        'id': pk,
    }
    return render(request, 'manager_topic/statistics.html', context)
