# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dj_bbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='admin',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_type',
        ),
        migrations.RemoveField(
            model_name='news',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='new',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='user',
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='News',
        ),
        migrations.DeleteModel(
            name='NewsType',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.DeleteModel(
            name='UserType',
        ),
    ]
