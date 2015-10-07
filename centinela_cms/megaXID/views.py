from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
from django.conf import settings
from django.utils import timezone
import datetime

from .models import Artist
from centinela.models import Slider
from .forms import ArtistForm


class ArtistCreate(generic.CreateView):
    form_class = ArtistForm
    template_name = 'megaXID/artist_form.html'
    success_url = '/megaXID/artist/success'

    def get_context_data(self, **kwargs):
        context = super(ArtistCreate, self).get_context_data(**kwargs)
        sliders = Slider.objects.filter(location='news').order_by('order')
        context['active_sliders_list'] = sliders
        context['site'] = settings.CENTINELA
        return context


class SuccessView(generic.TemplateView):
    template_name = 'megaXID/register_artist_success.html'

    def get_context_data(self):
        context = super(SuccessView, self).get_context_data()
        sliders = Slider.objects.filter(location='news').order_by('order')
        context['active_sliders_list'] = sliders
        context['site'] = settings.CENTINELA
        return context

# Create your views here.
