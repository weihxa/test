# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_bbs', '0004_blogspost_image_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogspost',
            name='image_urls',
            field=models.ImageField(upload_to=b'/static/images'),
        ),
    ]
