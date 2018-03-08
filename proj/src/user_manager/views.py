# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def user_home(request):
    return HttpResponse('This is user homepage')