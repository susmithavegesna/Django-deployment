# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-02 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Usertab',
        ),
    ]
