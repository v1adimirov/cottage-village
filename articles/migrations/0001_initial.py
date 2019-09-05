# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(choices=[(b'news', '\u041d\u043e\u0432\u043e\u0441\u0442\u044c'), (b'articles', '\u0421\u0442\u0430\u0442\u044c\u044f')], max_length=10, verbose_name='\u0442\u0438\u043f \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
                ('title', models.CharField(max_length=255, verbose_name='\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('image', models.ImageField(upload_to=b'articles', verbose_name='\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('preview', tinymce.models.HTMLField(verbose_name='\u0430\u043d\u043e\u043d\u0441')),
                ('content', tinymce.models.HTMLField(verbose_name='\u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435')),
                ('is_active', models.BooleanField(default=True, verbose_name='\u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0439')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u0434\u0430\u0442\u0430 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438',
            },
        ),
    ]