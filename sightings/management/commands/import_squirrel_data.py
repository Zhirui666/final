import csv
import io

from django.core.management.base  import BaseCommand

from sightings.models import sightings

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args,**options):
        with open(options['csv_file']) as fp:
            data = fp.read().strip()
            reader = csv.DictReader(io.StringIO(data))
            data = list(reader)
    
        for item in data:
            squirrel=sightings(
                Longitude=item['x'],
                Latitude=item['y'],
                Unique_Squirrel_ID=item['unique_squirrel_id'],
                Shift=item['shift'],
                Date=item['date'][4:]+'-'+item['date'][:2]+'-'+item['date'][2:4],
                Age=item['age'],
                Primary_Fur_Color=item['primary_fur_color'],
                Location=item['location'],
                Specific_Location=item['specific_location'],
                Running=item['running'],
                Chasing=item['chasing'],
                Climbing=item['climbing'],
                Eating=item['eating'],
                Foraging=item['foraging'],
                Other_Activities=item['other_activities'],
                Kuks=item['kuks'],
                Quaas=item['quaas'],
                Moans=item['moans'],
                Tail_flags=item['tail_flags'],
                Tail_twitches=item['tail_twitches'],
                Approaches=item['approaches'],
                Indifferent=item['indifferent'],
                Runs_from=item['runs_from'],
                )
            squirrel.save()
