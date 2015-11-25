# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog_rankings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('views', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 11, 25, 5, 54, 19, 300901, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(to='blog_rankings.Category'),
        ),
    ]
