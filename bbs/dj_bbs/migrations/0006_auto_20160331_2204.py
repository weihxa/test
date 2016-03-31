# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_bbs', '0005_auto_20160331_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('summary', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('favor_count', models.IntegerField(default=0)),
                ('reply_count', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('image_urls', models.ImageField(upload_to=b'news')),
            ],
        ),
        migrations.AlterField(
            model_name='blogspost',
            name='image_urls',
            field=models.ImageField(upload_to=b'blog'),
        ),
    ]
