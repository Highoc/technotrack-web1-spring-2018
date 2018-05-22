# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-22 12:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager_topic', '0007_topic_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ('name', 'id'), 'verbose_name': '\u0422\u043e\u043f\u0438\u043a', 'verbose_name_plural': '\u0422\u043e\u043f\u0438\u043a\u0438'},
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440 \u0442\u043e\u043f\u0438\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='categories',
            field=models.ManyToManyField(related_name='topics', to='manager_category.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='\u0412 \u0430\u0440\u0445\u0438\u0432\u0435?'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=127, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u043f\u0438\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.TextField(max_length=40980, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0442\u043e\u043f\u0438\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f'),
        ),
    ]