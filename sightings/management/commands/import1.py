from django.core.management.base import BaseCommand
from sightings.models import sightings
from django.utils import timezone
import pandas as pd
import numpy as np
import csv

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
                        
    def handle(self, *args, **options):
        df = pd.read_csv(options['csv_file'])
        for item in df.iterrows():
            item=item[1]
            s = sightings(
                Latitude=item['y'],
                Longitude=item['x'],
                Unique_Squirrel_ID = item['unique_squirrel_id'],
                Shift = item['shift'],
                Date = timezone.datetime(int(str(item['date'])[-4:]),int(str(item['date'])[:2]),int(str(item['date'])[2:4])).date(),
                Age = item['age'],
                Primary_Fur_Color = item['primary_fur_color'],
                Location = item['location'],                                                           
                Specific_Location = item['specific_location'],
                Running = item['running'],
                Chasing = item['chasing'],
                Climbing = item['climbing'],
                Eating = item['eating'],
                Foraging = item['foraging'],
                Other_Activities = item['other_activities'],
                Kuks = item['kuks'],
                Quaas = item['quaas'],
                Moans = item['moans'],
                Tail_flags = item['tail_flags'],
                Tail_twitches = item['tail_twitches'],
                Approaches = item['approaches'],
                Indifferent = item['indifferent'],
                Runs_from = item['runs_from'],
                )
            s.save()                                                         
