# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 22:51
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='preview',
            field=tinymce.models.HTMLField(blank=True, verbose_name='\u043a\u0440\u0430\u0442\u043a\u043e\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435'),
        ),
    ]
