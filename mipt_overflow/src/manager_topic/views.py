# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, reverse
from django import forms
from django.views.generic import CreateView, UpdateView
from .models import Topic
from django.forms import ModelForm
from comments.models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


def topic_list(request):
    topics = Topic.objects.all()

    form = TopicsListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data

        if data['sort']:
            topics = topics.order_by(data['sort'])

        if data['search']:
            topics = topics.filter(name__icontains=data['search'])

        if data['category']:
            topics = topics.filter(categories__name__icontains=data['category'])
    context = {
        'topics': topics,
        'topics_form': form,
    }

    return render(request, 'manager_topic/list.html', context)


def topic_detail(request, pk=None):

    topic = get_object_or_404(Topic, id=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data

        comment = form.save(commit=False)
        comment.author = request.user
        comment.topic_id = pk

        comment.save()

    context = {
        'topic': topic,
        'comment_form': form,
        'comments': topic.topic_comments.all().filter(is_archive=False).filter(comment=None).order_by('created')
    }

    return render(request, 'manager_topic/detail.html', context)


def topic_remove(request, pk=None):

    topic = get_object_or_404(Topic, id=pk, author=request.user)

    context = {
        'topic': topic
    }
    return render(request, 'manager_topic/remove.html', context)


class TopicsListForm(forms.Form):

    sort = forms.ChoiceField(
        choices=(
            ('name', 'Name asc'),
            ('-name', 'Name desc'),
            ('id', 'By Id'),
            ('created', 'By date'),
        ),
        required=False)
    category = forms.CharField(required=False)
    search = forms.CharField(required=False)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'comment']


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('name', 'categories', 'text')

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))


class TopicAdd(CreateView):
    form_class = TopicForm
    template_name = 'manager_topic/add.html'
    context_object_name = 'topic'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TopicAdd, self).form_valid(form)

    def get_success_url(self):
        return reverse('manager_topic:detail', kwargs={'pk': self.object.pk})


class TopicEdit(UpdateView):
    form_class = TopicForm
    model = Topic
    template_name = 'manager_topic/edit.html'
    context_object_name = 'topic'

    def get_queryset(self):
        queryset = super(TopicEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('manager_topic:detail', kwargs={'pk': self.object.pk})
