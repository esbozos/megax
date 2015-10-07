# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megaXID', '0002_auto_20151007_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='avatar',
            field=models.ImageField(upload_to='media/artist/profile/', verbose_name='Profile Photo'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='email',
            field=models.EmailField(verbose_name='Email', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='id_number',
            field=models.CharField(verbose_name='Document ID', max_length=100, unique=True),
        ),
    ]
