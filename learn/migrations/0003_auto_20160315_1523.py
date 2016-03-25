# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0002_asset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
