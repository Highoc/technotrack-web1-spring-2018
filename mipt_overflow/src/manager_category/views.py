# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def category_index(request):
    return render(request, 'manager_category/index.html')

def category_list(request):
    context = {}
    context['categories'] = [
        {'id': 1, 'name': 'Category #1'},
        {'id': 2, 'name': 'Category #2'},
        {'id': 3, 'name': 'Category #3'},
    ]
    return render(request, 'manager_category/list.html', context)

def category_detail(request, pk=None):
    context = {}
    context['category'] = {
        'name' : 'Category #{}'.format(pk),
        'id' : pk,
    }
    context['topics'] = [
        {
            'name': 'Topic #1',
            'id': '1',
        }, {
            'name': 'Topic #2',
            'id': '2',
        }, {
            'name': 'Topic #3',
            'id': '3',
        }
    ]
    return render(request, 'manager_category/detail.html', context)

def category_list_statictics(request):
    return render(request, 'manager_category/list_statistics.html')

def category_statistics(request, pk=None):
    context = {}
    context['category'] = {
        'name' : 'Category #{}'.format(pk),
        'id' : pk,
    }
    return render(request, 'manager_category/statistics.html', context)

def category_add(request):
    return render(request, 'manager_category/add.html')

def category_remove(request, pk=None):
    context = {}
    context['category'] = {
        'name' : 'Category #{}'.format(pk),
        'id' : pk,
    }
    return render(request, 'manager_category/remove.html', context)
