# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.utils.text


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('experience', models.TextField()),
                ('publish', models.BooleanField(default=True)),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', slugify=django.utils.text.slugify, editable=True)),
            ],
            options={
                'ordering': ['-title'],
            },
        ),
    ]
