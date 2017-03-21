# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(20)])),
                ('content', models.CharField(max_length=300, validators=[django.core.validators.MinLengthValidator(20)])),
                ('image_url', models.URLField()),
                ('timing', models.DateTimeField()),
                ('query', models.TextField(validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
    ]
