# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-18 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('press', '0018_auto_20181123_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='press',
            name='is_secure',
            field=models.BooleanField(default=False, help_text='If the site should redirect to HTTPS, mark this.'),
        ),
    ]