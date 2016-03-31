# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_bbs', '0002_auto_20160331_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='favor_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blogspost',
            name='reply_count',
            field=models.IntegerField(default=0),
        ),
    ]
