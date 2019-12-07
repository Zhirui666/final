
from django.core.management.base import BaseCommand, CommandError
from sightings.models import sightings
import pandas as pd
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)    
    def handle(self, *args, **options):
        path=options['csv_file']
        df=pd.read_csv(path, cols=['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
        name=['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age','Primary_Fur_Color','Location','Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from']
        for index,row in df.iterrows():          
                obj=sightings()
                for i,field in enumerate(row):
                    setattr(obj,field_name[i],field)
                obj.save()
           
