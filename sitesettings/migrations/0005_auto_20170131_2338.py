# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-31 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0004_auto_20170131_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='robots_txt',
            field=models.TextField(default='/', verbose_name='robots.txt'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='sitemap_xml',
            field=models.FileField(blank=True, null=True, upload_to=b'sitemap', verbose_name='sitemap.xml'),
        ),
    ]
