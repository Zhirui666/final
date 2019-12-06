# map/model.py
from django.db import models
from django.utils.translation import gettext as _

class sighting(models.Model):
    Latitude = models.DecimalField(
            max_digits = 100,
            decimal_places = 10,
            help_text = _("Latitude"),
            )
    Longitude = models.DecimalField(
            max_digits = 100,
            decimal_places = 10,
            help_text = _("Longitude"),
            )
    Unique_Squirrel_ID = models.DecimalField(
            max_digits = 100,
            help_text = _("Squirrel ID"),
            )
    
    PM = 'PM'
    AM = 'AM'
    
    SHIFT_CHOICES = (
        (PM, 'PM'),
        (AM, 'AM'),
        )
    
    Shift = models.CharField(
        max_length = 100,
        choices = SHIFT_CHOICES,
        )
    
    Date = models.DateField(
        help_text = _('Date'),
        )
    
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Other = 'Other'
    
    AGE_CHOICES = (
        (),
        (),
        (),
        )
    
    
