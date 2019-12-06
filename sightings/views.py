
from django.shortcuts import render,redirect
from .models import sightings
from django.http import HttpResponse
from django.http import Http404

def first(request):
    try:
        Sightings=sightings.objects.all()
    except:
        raise Http404("No such squirrel!")
    return render(request,'sightings/first.html',{'sightings':Sightings})


def add(request):
    if request.method=="POST":
        if request.POST.get('latitude') and request.POST.get('longitude') and request.POST.get('unique_squirrel_id'):            
            squirrel=sightings()
            squirrel.Longitude=request.POST.get('Longitude')
            squirrel.Latitude=request.POST.get('latitude')
            squirrel.Unique_Squirrel_ID=request.POST.get('unique_squirrel_id')
            squirrel.Shift=request.POST.get('shift')
            squirrel.Date=request.POST.get('date')
            squirrel.Age=request.POST.get('age')
            squirrel.Primary_Fur_Color=request.POST.get('primary_fur_color')
            squirrel.Location=request.POST.get('location')
            squirrel.Specific_Location=request.POST.get('specific_location')
            squirrel.Running=request.POST.get('running')
            squirrel.Chasing=request.POST.get('chasing')
            squirrel.Climbing=request.POST.get('climbing')
            squirrel.Cating=request.POST.get('eating')
            squirrel.Foraging=request.POST.get('foraging')
            squirrel.Other_Activities=request.POST.get('other_activities')
            squirrel.Kuks=request.POST.get('kuks')
            squirrel.Quaas=request.POST.get('quaas')
            squirrel.Moans=request.POST.get('moans')
            squirrel.Tail_flags=request.POST.get('tail_flags')
            squirrel.Tail_twitches=request.POST.get('tail_twitches')
            squirrel.Approaches=request.POST.get('approaches')
            squirrel.Indifferent=request.POST.get('indifferent')
            squirrel.Runs_from=request.POST.get('runs_from')
            squirrel.save()
            context={'sightings':sightings.objects.all(),}
            return render(request,'sightings/index.html',context)
    elif request.method=="GET":
            return render(request,'sightings/add.html')

def details(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {'squirrel':squirrel,}
    return render(request,'sightings/details.html',context)

def stats(request):
    sightings_stats1=sightings.objects.all().count()
    sightings_stats2=sightings.objects.filter(Primary_Fur_Color='Black').count()
    sightings_stats3=sightings.objects.filter(Running='True').count()
    sightings_stats4=sightings.objects.filter(Age='Adult').count()
    sightings_stats5=sightings.objects.filter(Age='Juvenile').count()
    context={
            'Number of all the sightings':sightings_stats1,
            'Number of black primary fur color sightings':sightings_stats2,
            'Number of running sightings':sightings_stats3,
            'Number of adult sightings':sightings_stats4,
            'Number of juvenile sightings':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)

def update(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        squirrel.Longitude=request.POST.get['longitude']
        squirrel.Latitude=request.POST.get['latitude']
        squirrel.Shift=request.POST.get['shift']
        squirrel.Date=request.POST.get['date']
        squirrel.Age=request.POST.get['age']
        squirrel.Primary_Fur_Color=request.POST.get['primary_fur_color']
        squirrel.Location=request.POST.get['location']
        squirrel.Specific_Location=request.POST.get['specific_location']
        squirrel.Running=request.POST.get['running']
        squirrel.Chasing=request.POST.get['chasing']
        squirrel.Climbing=request.POST.get['climbing']
        squirrel.Eating=request.POST.get['eating']
        squirrel.Foraging=request.POST.get['foraging']
        squirrel.Other_activities=request.POST.get['other_activities']
        squirrel.Kuks=request.POST.get['kuks']
        squirrel.Quaas=request.POST.get['quaas']
        squirrel.Moans=request.POST.get['moans']
        squirrel.Tail_flags=request.POST.get['tail_flags']
        squirrel.Tail_twitches=request.POST.get['tail_twitches']
        squirrel.Approaches=request.POST.get['approaches']
        squirrel.Indifferent=request.POST.get['indifferent']
        squirrel.Runs_from=request.POST.get['runs_from']
        squirrel.save()
        context={'squirrel':squirrel,}
        return render(request,'sightings/details.html',context)
    elif request.method=="GET":
        context={'squirrel':squirrel,}
        return render(request,'sightings/update.html',context)
