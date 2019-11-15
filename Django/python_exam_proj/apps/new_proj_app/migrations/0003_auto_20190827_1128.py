# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-27 16:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_proj_app', '0002_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='new_proj_app.User'),
        ),
    ]
