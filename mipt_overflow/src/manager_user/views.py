# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def user_index(request):
    return render(request, 'manager_user/index.html')

def user_info(request):
    return render(request, 'manager_user/info.html')