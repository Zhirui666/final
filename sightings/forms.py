from django.forms import ModelForm
from .models import sightings_model
class SquForm(ModelForm):
    class Meta:
        model = sightings_model
        fields = '__all__'
