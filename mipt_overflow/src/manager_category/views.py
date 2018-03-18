# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def category_list(request):
    context = {}
    context['categories'] = [
        'Category 1',
        'Category 2',
        'Category 3'
    ]

    return render(request, 'manager_category/category_list.html', context)

def category_detail(request, pk=None):
    context = {}
    context['category'] = {
        'name' : 'Category #1',
        'id' : pk,
    }

    return render(request, 'manager_category/category_detail.html', context)
