# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_playlist_playlisttrack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlisttrack',
            old_name='artist',
            new_name='track',
        ),
        migrations.AddField(
            model_name='playlisttrack',
            name='play_list',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='customer.Playlist'),
            preserve_default=False,
        ),
    ]