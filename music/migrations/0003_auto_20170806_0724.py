# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 07:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('title',)},
        ),
    ]
