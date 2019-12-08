
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

# def AddView(request):
#     if request.method =='POST':
#         form = SightingsForm(request.POST)
#         #check data with form
#         if form.is_valid():
#             form.save()
#             return redirect(f'/sightings/all.html')
#         else:
#             context= {'form': form,
#                       'error': 'The form was not valid. Please do it again.'}
#             return render(request,'sightings/edit.html' , context)
#     else:
#         form = SightingsForm()
#     context = {
#             'form':form,
#     }
#     return render(request,'sightings/add.html',context)

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


def details(request):
    squirrel_id = list()
    for i in sightings_model.objects.all():
        i_dict = {}
        i_dict['sid']=i.squirrel_id
        squirrel_id.append(i_dict)
    return render(request, 'sightings/details.html', {'squirrel_id':squirrel_id})

    


# def edit(request, Unique_Squirrel_ID):
#     information = sightings.objects.get(Unique_Squirrel_ID = Unique_Squirrel_ID)
#     if request.method == "POST":
#         if 'delete' in request.POST:
#             information.delete()
#         else:
#             list_=list(request.POST.values())[1:]
#             squirrel=sightings.objects.filter(Unique_Squirrel_ID = Unique_Squirrel_ID)
#             information= SquTable(request.POST, instance = squirrel[0])
#             if information.is_valid():
#                 model=apps.get_model('sightings','sightings')
#                 names = [a.name for a in model._meta.fields][1:]
#                 for s in squirrel:
#                     for index, field in enumerate(names):
#                         if list_[index]:
#                             setattr(s, field, list_[index])
#                     s.save()
#         return redirect('/sightings/')
#     return render(request,'sightings/edit.html',{'information':information})

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

# def edit(request,Unique_Squirrel_ID):
#     information = sightings_model.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
#    # details = get_object_or_404(squ_model,Unique_Squirrel_ID=Unique_Squirrel_ID)
#     if request.method == "POST":
#         if 'delete' in request.POST:
#             information.delete()
#         else:
#             list_=list(request.POST.values())[1:]
#             sqs = sightings_model.objects.filter(Unique_Squirrel_ID=Unique_Squirrel_ID)
#             information = SquForm(request.POST,instance=sqs[0])
#             if information.is_valid():
#                 model=apps.get_model('sightings','sightings_model')
#                 field_names = [f.name for f in model._meta.fields][1:]
#                 for sq in sqs:
#                     for idx,f in enumerate(field_names):
#                         if list_[idx]:
#                             setattr(sq,f,list_[idx])
#                     sq.save()
#         return redirect('/sightings/')
#     return render(request, 'sightings/edit.html',{'information':information})

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
