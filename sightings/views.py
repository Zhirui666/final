
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from .models import sightings_model
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .forms import SquForm
from django.forms import ModelForm
from django.db.models import Count, Q


def index(request):
    squirrels = sightings_model.objects.all()
    context = {'squirrels': squirrels,}
    return render(request,'sightings/index.html', context)



def add(request):
    if request.method=='POST':
        form = SquForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquForm()
        
    context = {
            'form': form,
    }
    return render(request, 'sightings/add.html',context)

       
    

def map(request):
    squirrels=sightings_model.objects.all()[:100]
    return render(request, 'sightings/map.html', {'squirrels':squirrels})


def edit(request,Unique_Squirrel_ID):
    information = sightings_model.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        form = SquForm(request.POST, instance=information)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquForm(instance=information)
    context = {
        'form': form,
    }
        
    return render(request, 'sightings/add.html',context)



def stats(request):
    Totals=sightings_model.objects.all().count()
    Running=sightings_model.objects.filter(Running='True').count()
    Eating=sightings_model.objects.filter(Eating='True').count()
    Adults=sightings_model.objects.filter(Age='Adult').count()
    Gray=sightings_model.objects.filter(Primary_Fur_Color='Gray').count()
    context={
            'Totals':Totals,
            'Running':Running,
            'Eating':Eating,
            'Adults':Adults, 
            'Gray':Gray,
            }
    return render(request, 'sightings/stats.html', context)

