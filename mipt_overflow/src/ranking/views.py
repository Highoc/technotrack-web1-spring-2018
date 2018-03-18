# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def ranking(response):
    return HttpResponse('This is ranking_list page')