# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megaXID', '0003_auto_20151007_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='active',
            field=models.BooleanField(verbose_name='Active', default=False),
        ),
        migrations.AlterField(
            model_name='artist',
            name='avatar',
            field=models.ImageField(upload_to='artist/profile/%Y/%m/%d', verbose_name='Profile Photo'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='work1',
            field=models.ImageField(upload_to='artist/demo/%Y/%m/%d', help_text='show us your best art work', verbose_name='Photo of your work #1'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='work2',
            field=models.ImageField(upload_to='artist/demo/%Y/%m/%d', verbose_name='Photo of your work #2'),
        ),
    ]
