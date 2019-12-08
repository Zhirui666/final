from django.db import models
from django.utils.translation import gettext as _

from django.utils import timezone

class sightings_model(models.Model):
    Longitude = models.DecimalField(
            help_text='Longitude',
            max_digits=16,
            decimal_places=13,
            )
    Latitude = models.DecimalField(
            help_text='Latitude',
            max_digits=16,
            decimal_places=13,
            )

    Unique_Squirrel_ID = models.CharField(
            max_length = 100,
            help_text = _("Unique_Squirrel_ID"),
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
        max_length=100,
        blank=True,
        null=True,
        )
    
    
    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Other = 'Other'
    
    AGE_CHOICES = (
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
        (Other, 'Other'),
        )
    
    Age = models.CharField(
        max_length = 10,
        choices = AGE_CHOICES,
        help_text = _('Age'),
        )
    
    Black = 'Black'
    Cinnamon = 'Cinnamon'
    Gray = 'Gray'
    Other = 'Other'
    
    PRIMARY_FUR_COLOR_CHOICES = (
        (Black, 'Black'),
        (Cinnamon, 'Cinnamon'),
        (Gray, 'Gray'),
        (Other, 'Other'),
        )
    
    Primary_Fur_Color = models.CharField(
            max_length = 30,
            choices = PRIMARY_FUR_COLOR_CHOICES,
            help_text = _('Primary_Fur_Color'),
            )
    
    Above_Ground = 'Above Ground'
    Ground_Plane = 'Ground Plane'
    Other = 'Other'
    
    LOCATION_CHOICES = (
        (Above_Ground, 'Above Ground'),
        (Ground_Plane, 'Ground Plane'),
        (Other, 'Other'),
        )
    
    Location = models.CharField(
        max_length = 30,
        choices = LOCATION_CHOICES,
        help_text = _('Location'),
        )
    
    Specific_Location = models.CharField(
        max_length=100,
        help_text = _('Specific_Location'),
        )
    
    Running = models.BooleanField(
        help_text = _('Running'),
        )
    
    Chasing = models.BooleanField(
        help_text = _('Chasing'),
        )
    
    Climbing = models.BooleanField(
        help_text = _('Climbing'),
        )
    
    Eating = models.BooleanField(
        help_text = _('Eating'),
        )
    
    Foraging = models.BooleanField(
        help_text = _('Foraging'),
        )
    
    Other_Activities = models.CharField(
        max_length=100,
        help_text = _('Other_Activities'),
        )
    
    Kuks = models.BooleanField(
        help_text = _('Kuks'),
        )
    
    Quaas = models.BooleanField(
        help_text = _('Quaas'),
        )
    
    Moans = models.BooleanField(
        help_text = _('Moans'),
        )
    
    Tail_flags = models.BooleanField(
        help_text = _('Tail_flags'),
        )
    
    Tail_twitches = models.BooleanField(
        help_text = _('Tail_twitchs'),
        )
    
    Approaches = models.BooleanField(
        help_text = _('Approaches'),
        )
    
    Indifferent = models.BooleanField(
        help_text = _('Indifferent'),
        )
    
    Runs_from = models.BooleanField(
        help_text = _('Runs_from'),
        )
    def __str__(self):
         return self.Unique_Squirrel_ID
