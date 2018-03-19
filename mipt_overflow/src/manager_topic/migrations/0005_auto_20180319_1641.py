# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 16:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager_topic', '0004_auto_20180319_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='is_arhive',
        ),
        migrations.AddField(
            model_name='topic',
            name='is_archive',
            field=models.BooleanField(default=False, verbose_name='Topic is archived'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL, verbose_name='Author_name'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='categories',
            field=models.ManyToManyField(related_name='topics', to='manager_category.Category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=127, verbose_name='Topic_name'),
        ),
    ]