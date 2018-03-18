# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def core_index(request):
    return render(request, 'core/index.html')

def core_login(request):
    return render(request, 'core/login.html')

def core_logout(request):
    return render(request, 'core/logout.html')

def core_register(request):
    return render(request, 'core/register.html')
