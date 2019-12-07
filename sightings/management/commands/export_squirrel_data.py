import csv
from sightings.models import squirrel
from django.utils.encoding import a
from django.core.management import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('position')

    def handle(self,*args,**kargs):
        with open(kargs['position']
            w=csv.writer(csvfile)
            w.writerow([
                a(u"Unique_Squirrel_ID"),
                a(u"Longitude"),
                a(u"Latitude"),
                a(u"Shift"),
                a(u"Date"),
                a(u"Age"),
                a(u"Primary_fur_color"),
                a(u"Location"),
                a(u"Specific_location"),
                a(u"Running"),
                a(u"Chasing"),
                a(u"Climbing"),
                a(u"Eating"),
                a(u"Foraging"),
                a(u"Other_Activities"),
                a(u"Kuks"),
                a(u"Quaas"),
                a(u"Moans"),
                a(u"Tail_flags"),
                a(u"Tail_twitches"),
                a(u"Approaches"),
                a(u"Indifferent"),
                a(u"Runs_from"),
                ])
            for s in squirrel.objects.values():
                w.writerow([
                    a(s['Unique_Squirrel_ID']),
                    a(s["Longitude"]),
                    a(s["Latitude"]),
                    a(s["Shift"]),
                    a(s["Date"]),
                    a(s["Age"]),
                    a(s["Primary_fur_color"]),
                    a(s["Location"]),
                    a(s["Specific_location"]),
                    a(s["Running"]),
                    a(s["Chasing"]),
                    a(s["Climbing"]),
                    a(s["Eating"]),
                    a(s["Foraging"]),
                    a(s["Other_Activities"]),
                    a(s["Kuks"]),
                    a(s["Quaas"]),
                    a(s["Moans"]),
                    a(s["Tail_flags"]),
                    a(s["Tail_twitches"]),
                    a(s["Approaches"]),
                    a(s["Indifferent"]),
                    a(s["Runs_from"]),])
