from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.conf import settings
from django.utils import timezone
import datetime

from .models import Artist
from .forms import ArtistForm


class ArtistCreate(generic.CreateView):
    form_class = ArtistForm
    template_name = 'megaXID/artist_form.html'
    success_url = '/megaXID/artist/success'


class SuccessView(generic.TemplateView):
    template_name = 'megaXID/register_artist_success.html'

# Create your views here.
