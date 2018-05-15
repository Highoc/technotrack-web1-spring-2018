# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-14 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager_category', '0003_category_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name', 'id'), 'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.AddField(
            model_name='category',
            name='is_hidden',
            field=models.BooleanField(default=False, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0441\u043a\u0440\u044b\u0442\u0430?'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=4096, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=127, verbose_name='\u0422\u0435\u043c\u0430 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
    ]
