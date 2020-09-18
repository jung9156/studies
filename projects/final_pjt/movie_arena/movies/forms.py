from .models import Movie, Genre
from django import forms


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['genre', 'like_users']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
