# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=250, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last Name')),
                ('nick_name', models.CharField(blank=True, max_length=200, help_text='if people know you by a nickname, or want to introduce one. please indicate now.', verbose_name='Nickname')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=20, verbose_name='Gender')),
                ('birth_day', models.DateField(verbose_name='Birthday')),
                ('phone', models.CharField(max_length=200, verbose_name='Phone')),
                ('address', models.TextField(verbose_name='Address')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name=['VE'])),
                ('web_places', models.TextField(help_text='List of your personal and professional websites, socials accounts and others.', verbose_name='Web places')),
                ('skills', models.TextField(help_text='tell us about your skills on body art.', verbose_name='Skills')),
                ('years_experience', models.IntegerField(verbose_name='Years experience')),
                ('applied', models.BooleanField(verbose_name='have you applied to the show before?')),
                ('avatar', models.ImageField(width_field=400, upload_to='media/artist/profile/', verbose_name='Profile Photo')),
                ('work1', models.ImageField(help_text='show us your best art work', upload_to='', verbose_name='Photo of your work #1')),
                ('work2', models.ImageField(upload_to='', verbose_name='Photo of your work #2')),
                ('payment', models.TextField(help_text='please indicate reference number, date, bank and amount of your payment.', verbose_name='Payment details')),
                ('accept_terms', models.BooleanField(verbose_name='By clicking "Yes" bellow you have acknowledged and agreed to the terms and conditions.')),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
            ],
            options={
                'verbose_name_plural': 'artists',
                'verbose_name': 'artist',
            },
        ),
    ]
