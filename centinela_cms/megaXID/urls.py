from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^create/$', views.ArtistCreate.as_view(), name='create'),
    url(r'^artist/success', views.SuccessView.as_view(), name='success')
]

urlpatterns += staticfiles_urlpatterns()