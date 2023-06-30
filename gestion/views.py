from django.shortcuts import get_object_or_404, render, redirect
from gestion.forms import *
from django.core.paginator import Paginator
from  django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from  django.views.decorators.cache import cache_control 
from datetime import date, datetime
from django.db import transaction, models
from django.db.models import Count, Sum
from num2words import num2words





def archive(request):
    archives = Tache.objects.all()
    context = {"archives":archives}
    return render(request, 'gestion/archives/archive.html', context)





def add_archive(request):
    if request.method=="POST":
        form = TacheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            tache = form.cleaned_data['analyse']
            messages.success(request, f"Archives {tache} ajouté !")
            return redirect('archive')
        else:
            return render(request, 'gestion/archives/add.html', {"form":form})
    else:
        current_year = datetime.now().year
        form = TacheForm(initial={'year_field': str(current_year)})
    return render(request, 'gestion/archives/add.html', {"form":form})





def edit_archive(request):
    archive = Tache.objects.get(id=id)
    if request.method == 'POST':
        form = TacheForm(request.POST, instance=archive)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Modification {archive } effectué avec susccès!")
            return redirect('archive')
    else:
        form = TacheForm(instance=archive)
    return render(request, 'gestion/archives/edit.html', {"form":form, 'archive':archive})




def delete_archive(request):
    archive = Tache.objects.get(id = id)
    if request.method=='POST':
        archive.delete()
        messages.success(request, f'Aarchive {archive } supprimer avec susccès !')
        return redirect("archive")
    return render(request, 'gestion/archives/delete.html', {'archive':archive})




def search(request):
    archives = Tache.objects.all()
    context = {"archives":archives}
    return render(request, 'gestion/consultation/search.html', context)