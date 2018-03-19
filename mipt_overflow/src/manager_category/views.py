# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Category

def category_index(request):
    return render(request, 'manager_category/index.html')

def category_list(request):
    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'manager_category/list.html', context)

def category_detail(request, pk=None):
    category = Category.objects.get(id=pk)

    context = {
        'category': category,
        'topics': category.topics.all().filter(is_archive=False)
    }
    return render(request, 'manager_category/detail.html', context)

def category_list_statictics(request):
    return render(request, 'manager_category/list_statistics.html')

def category_statistics(request, pk=None):
    context = {
        'category': Category.objects.get(id=pk)
    }
    return render(request, 'manager_category/statistics.html', context)

def category_add(request):
    return render(request, 'manager_category/add.html')

def category_remove(request, pk=None):
    context = {
        'category': Category.objects.get(id=pk)
    }
    return render(request, 'manager_category/remove.html', context)
