
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from .models import sightings
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from .forms import SquTable
from django.forms import ModelForm
from django.db.models import Count


def index(request):
    sightings_ = sightings.objects.all()
    context = {'sightings': sightings_,}
    return render(request,'sightings/index.html', context)

def add(request):
    if request.method=='POST':
        table = SquTable(request.POST)
        if table.is_valid():
            table.save()
            return redirect(f'/sightings/')
    else:
        table = SquTable()

    context = {'table': table}

    return render(request, 'sightings/add.html', context)

def edit(request, Unique_Squirrel_ID):
    information = sightings.objects.get(Unique_Squirrel_ID = Unique_Squirrel_ID)
    if request.method == "POST":
        if 'delete' in request.POST:
            information.delete()
        else:
            list_=list(request.POST.values())[1:]
            squirrel=sightings.objects.filter(Unique_Squirrel_ID = Unique_Squirrel_ID)
            information= SquTable(request.POST, instance = squirrel[0])
            if information.is_valid():
                model=apps.get_model('sightings','sightings')
                names = [a.name for a in model._meta.fields][1:]
                for s in squirrel:
                    for index, field in enumerate(names):
                        if list_[index]:
                            setattr(s, field, list_[index])
                    s.save()
        return redirect('/sightings/')
    return render(request,'sightings/edit.html',{'information':information})


def stats(request):
    Totals=sightings.objects.all().count()
    Running=sightings.objects.filter(Running='True').count()
    Eating=sightings.objects.filter(Eating='True').count()
    Adults=sightings.objects.filter(Age='Adult').count()
    Gray=sightings.objects.filter(Primary_Fur_Color='Gray').count()
    context={
            'Totals':Totals,
            'Running':Running,
            'Eating':Eating,
            'Adults':Adults, 
            'Gray':Gray,
            }
    return render(request, 'sightings/stats.html', context)

#def update(request,Unique_Squirrel_ID):
#    sightings_ = get_object_or_404(sightings, Unique_Squirrel_ID=Unique_Squirrel_ID)
 #   if request.method=="POST":
  #      table = SquTable(request.POST, instance=sightings_)
   #     if table.is_valid():
    #        table.save()
     #       sightings_ = sightings.objects.all()
      #      context = {'sightings': sightings_,}
         #   return render(request,'sightings/index.html',context)
    #context = {'table':table, }
    # return render(request, 'sightings/update.html',context)
