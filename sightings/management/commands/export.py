from django.core.management.base import BaseCommand, CommandError
import csv
from django.apps import apps
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
    def handle(self, *args, **options):
        
        path=options['csv_file']
        f=open(path,'w+')
        model=apps.get_model('vwsquirrel','sq_model')
        field_names=['Latitude','Longitude','Unique_Squirrel_ID','Shift','Date','Age','Primary_Fur_Color','Location','Specific_Location','Running','Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks','Quaas','Moans','Tail_flags','Tail_twitches','Approaches','Indifferent','Runs_from']
        writer = csv.writer(f)
        writer.writerow(field_names)
        for instance in model.objects.all():
            writer.writerow([getattr(instance, f) for f in field_names])
        f.close()
