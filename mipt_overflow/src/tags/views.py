# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def tags(request):
    return HttpResponse('This is tags page')