from django.forms import ModelForm
from .models import sightings
class SquTable(ModelForm):
    class Change:
        model = sightings
        fields = '__all__'
