from django.forms import ModelForm
from .models import sightings
class SquForm(ModelForm):
    class Meta:
        model = sightings
        fields = '__all__'
