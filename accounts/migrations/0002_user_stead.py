# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-05 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0006_auto_20170201_2113'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plan.Stead', verbose_name='\u0443\u0447\u0430\u0441\u0442\u043e\u043a'),
        ),
    ]
