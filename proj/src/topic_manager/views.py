# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def topic_detail(request, category_id):
    return HttpResponse('This is topic {}'.format(category_id))

def topic_list(request):
    return HttpResponse('This is topic_list')

def topic_add(request):
    return HttpResponse('This is topic_add')