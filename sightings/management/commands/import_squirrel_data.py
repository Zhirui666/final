import csv
from django.core.management import BaseCommand

from sightings.models import sightings

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args,**kargs):
        path=kargs['csv_file']
        with open(kargs['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
    
        for item in data:
            squirrel=sightings(
                Unique_Squirrel_ID=item['Unique Squirrel ID'],
                Longitude=item['X'],
                Latitude=item['Y'],
                Shift=item['Shift'],
                Date=item['Date'][4:]+'-'+item['Date'][:2]+'-'+item['Date'][2:4],
                Age=item['Age'],
                Primary_fur_color=item['Primary_Fur_Color'],
                Location=item['Location'],
                Specific_location=item['Specific_Location'],
                Running=item['Running'],
                Chasing=item['Chasing'],
                Climbing=item['Climbing'],
                Eating=item['Eating'],
                Foraging=item['Foraging'],
                Other_Activities=item['Other_Activities'],
                Kuks=item['Kuks'],
                Quaas=item['Quaas'],
                Moans=item['Moans'],
                Tail_flags=item['Tail_flags'],
                Tail_twitches=item['Tail_twitches'],
                Approaches=item['Approaches'],
                Indifferent=item['Indifferent'],
                Runs_from=item['Runs_from'],
                )
            squirrel.save()
