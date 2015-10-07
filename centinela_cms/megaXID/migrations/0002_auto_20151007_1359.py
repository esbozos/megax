# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('megaXID', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='artist',
            name='email',
            field=models.EmailField(default='no@no.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='id_number',
            field=models.CharField(default=1, max_length=100, verbose_name='Document ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artist',
            name='applied',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='have you applied to the show before?'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='birth_day',
            field=models.DateField(help_text='format DD/MM/YYYY', verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='artist',
            name='web_places',
            field=models.TextField(help_text='List of your personal and professional websites, socials accounts and others.', blank=True, verbose_name='Web places'),
        ),
    ]
