# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dj_bbs', '0007_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(default=b'123'),
        ),
    ]
