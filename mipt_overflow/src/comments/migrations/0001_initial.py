# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 17:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manager_topic', '0006_auto_20180319_1654'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2047, verbose_name='Comment text')),
                ('is_archive', models.BooleanField(default=False, verbose_name='Comment is archived')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updation date')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_comments', to=settings.AUTH_USER_MODEL, verbose_name='Author name')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='comments.Comment', verbose_name='Parent comment')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_comments', to='manager_topic.Topic', verbose_name='Topic')),
            ],
            options={
                'ordering': ('topic', 'author', 'id'),
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]