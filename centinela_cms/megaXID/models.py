from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField
from ckeditor.fields import RichTextField
from django.template import defaultfilters
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

GENDER_TYPES = [
    ('male', _('male')),
    ('female', _('female'))
]
# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(_('First Name'), max_length=250)
    last_name = models.CharField(_('Last Name'), max_length=250)
    id_number = models.CharField(_('Document ID'), max_length=100, unique=True)
    nick_name = models.CharField(_('Nickname'), max_length=200, help_text=_('if people know you by a nickname, or want to introduce one. please indicate now.'), blank=True)
    gender = models.CharField(_('Gender'), max_length=20, choices=GENDER_TYPES)
    birth_day = models.DateField(_('Birthday'), help_text=_('format DD/MM/YYYY'))
    email = models.EmailField(_('Email'), unique=True)
    phone = models.CharField(_('Phone'),max_length=200)
    address = models.TextField(_('Address'))
    country = CountryField()
    avatar = models.ImageField(_('Profile Photo'), upload_to='artist/profile/%Y/%m/%d')
    work1 = models.ImageField(_('Photo of your work #1'), help_text=_('show us your best art work'), upload_to='artist/demo/%Y/%m/%d')
    work2 = models.ImageField(_('Photo of your work #2'), upload_to='artist/demo/%Y/%m/%d')
    web_places = models.TextField(_('Web places'), blank=True, help_text=_('List of your personal and professional websites, socials accounts and others.'))
    skills = models.TextField(_('Skills'), help_text=_('tell us about your skills on body art.'))
    years_experience = models.IntegerField(_('Years experience'))
    applied = models.BooleanField(_('have you applied to the show before?'), choices=[(True, _('Yes')), (False, 'No')])
    payment = models.TextField(_('Payment details'), help_text=_('please indicate reference number, date, bank and amount of your payment.'))
    accept_terms = models.BooleanField(_('By clicking "Yes" bellow you have acknowledged and agreed to the terms and conditions.'))
    created_date = models.DateTimeField(_('Created at'), default=timezone.now)
    active = models.BooleanField(_('Active'), default=False)
    slug = models.CharField(_('slug'), max_length=100)

    def __unicode__(self):
        return self.first_name + '' + self.last_name

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        if hasattr(self, 'nick_name'):
            self.slug = defaultfilters.slugify(self.nick_name)
        else:
            self.slug = defaultfilters.slugify(self.first_name + ' ' + self.last_name)
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('artist')
        verbose_name_plural = _('artists')