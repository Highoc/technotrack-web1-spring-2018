# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.http import Http404
from .models import Category
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.cache import caches
from like.models import Like
from django.db.models import Q

cache = caches['default']

def category_list(request):

    categories = Category.objects.all()

    form = CategorySortForm(request.GET)

    if form.is_valid():
        data = form.cleaned_data

        if data['sort']:
            categories = categories.order_by(data['sort'])

        if data['search']:
            categories = categories.filter(name__icontains=data['search'])


    context = {
        'categories': categories,
        'categories_form': form,
    }

    return render(request, 'manager_category/list.html', context)


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    topics = category.topics.all().filter(is_archive=False)

    topics = topics.annotate_everything()

    for topic in topics:
        cache_key = 'post{}likescount'.format(topic.id)
        likes_count = cache.get(cache_key)

        if likes_count is None:
            likes_count = Like.objects.filter(Q(topic=topic)&Q(is_archive=False)).count()
            cache.set(cache_key, likes_count, 10)
        topic.likes_count = likes_count

    form = TopicSortForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data

        if data['sort']:
            topics = topics.order_by(data['sort'])

        if data['search']:
            topics = topics.filter(name__icontains=data['search'])

    context = {
        'category': category,
        'topics': topics,
        'topics_form': form,
    }

    return render(request, 'manager_category/detail.html', context)


def category_edit(request, pk=None):
    if not request.user.is_superuser:
        return Http404()

    category = get_object_or_404(Category, id=pk)

    context = {
        'category': category,
    }

    if request.method == 'GET':
        form = CategoryForm(instance=category)
        context['category_form'] = form
        return render(request, 'manager_category/edit.html', context)

    elif request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        context['category_form'] = form
        if form.is_valid():
            form.save()
            return redirect('manager_category:list')
        else:
            return render(request, 'manager_category/add.html', {'category_form': form})


def category_add(request):

    if not request.user.is_superuser:
        return Http404()

    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'manager_category/add.html', {'category_form': form} )

    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('manager_category:detail', pk=category.id)
        else:
            return render(request, 'manager_category/add.html', {'category_form': form})


def category_remove(request, pk=None):

    if not request.user.is_superuser:
        return Http404()

    category = get_object_or_404(Category, id=pk)

    context = {
        'category': category
    }
    return render(request, 'manager_category/remove.html', context)



class CategorySortForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('name', 'По теме'),
            ('-likes_count', 'По рейтингу'),
            ('id', 'По ID'),
            ('-created', 'По дате создания'),
        ),
        required=False
    )

    search = forms.CharField(
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(CategorySortForm, self).__init__(*args, **kwargs)
        self.fields['sort'].widget.attrs['class'] = 'form-control'
        self.fields['search'].widget.attrs['class'] = 'form-control'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

class TopicSortForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('name', 'По имени'),
            ('-likes_count', 'По рейтингу'),
            ('id', 'По ID'),
            ('-created', 'По дате создания'),
        ),
        required=False)
    search = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(TopicSortForm, self).__init__(*args, **kwargs)
        self.fields['sort'].widget.attrs['class'] = 'form-control'
        self.fields['search'].widget.attrs['class'] = 'form-control'