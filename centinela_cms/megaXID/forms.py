from django.forms import ModelForm
from .models import Artist


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = [
            'avatar',
            'first_name',
            'last_name',
            'id_number',
            'nick_name',
            'work1',
            'work2',
            'gender',
            'birth_day',
            'email',
            'phone',
            'address',
            'country',
            'web_places',
            'skills',
            'years_experience',
            'applied',
            'payment',
            'accept_terms',
        ]