from django.forms import ModelForm

from .models import Projection, Card

class ProjectionForm(ModelForm):
    class Meta:
        model = Projection
        fields = [
            'movie_name', 'movie_time', 'hall_capacity'
        ]

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['seat_number']