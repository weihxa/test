# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_bbs', '0008_auto_20160405_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
