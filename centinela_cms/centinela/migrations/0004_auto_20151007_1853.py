# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('centinela', '0003_auto_20150924_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgets',
            name='place',
            field=models.CharField(default='lateral', verbose_name='Place', max_length=30, choices=[('top', 'Top'), ('lateral', 'Lateral'), ('after_post', 'After Post'), ('before_post', 'Before Post'), ('footer', 'Footer')]),
        ),
        migrations.AlterField(
            model_name='slider',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 23, 23, 11, 195557, tzinfo=utc), verbose_name='until'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='status',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='widgets',
            name='until_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 23, 23, 11, 196898, tzinfo=utc), verbose_name='until'),
        ),
    ]
