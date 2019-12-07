from django.forms import ModelForm
from .models import sightings
class SquForm(ModelForm):
    class Meta:
        model = sightings_model
        fields = '__all__'
