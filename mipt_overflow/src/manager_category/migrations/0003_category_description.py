# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-14 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_category', '0002_auto_20180319_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e', max_length=4096, verbose_name='Category description'),
            preserve_default=False,
        ),
    ]
