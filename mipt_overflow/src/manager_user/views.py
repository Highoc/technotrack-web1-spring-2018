# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse

def index(reqest):
    return HttpResponse('This is index')

def user_home(request):
    return HttpResponse('This is user homepage')