# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

def comments(request):
    return HttpResponse('This is comments page')