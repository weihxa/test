# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_bbs', '0003_auto_20160331_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='image_urls',
            field=models.ImageField(default=b'/static/images/01.jpg', upload_to=b'images'),
        ),
    ]
