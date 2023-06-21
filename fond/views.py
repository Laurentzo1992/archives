from django.shortcuts import render
from fond.models import *
from fond.forms import *
from django.shortcuts import render
from  django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, permission_required
from  django.views.decorators.cache import cache_control 
from datetime import date, datetime
from django.db import transaction, models
from django.db.models import Count, Sum




def serie(request):
    series = Serie.objects.all()
    context = {'series':series}
    return render(request, 'fond/serie/serie.html', context)




def add_serie(request):
    if request.method=="POST":
        form = SerieForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['serie']
            messages.success(request, f"Serie {form_data} ajouter avec succès !")
            return redirect('serie')
        else:
            return render(request, 'fond/serie/add.html', {"form":form})
    else:
        form = SerieForm()
        return render(request, 'fond/serie/add.html', {"form":form})
    
    


def edit_serie(request, id):
    serie = Serie.objects.get(id=id)
    if request.method == 'POST':
        form = SerieForm(request.POST, instance=serie)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Serie {serie} modifiéé avec succès !")
            return redirect('serie')
    else:
        form = SerieForm(instance=serie)
    return render(request, 'fond/serie/edit.html',  {'form':form})




def delete_serie(request, id):
    serie = Serie.objects.get(id = id)
    if request.method=='POST':
        serie.delete()
        messages.success(request, f'Serie {serie} supprimer avec susccès !')
        return redirect("serie")
    return render(request, 'fond/serie/delete.html', {"serie":serie})





def sousserie(request):
    sousseries = Sous_serie.objects.all()
    context = {'sousseries':sousseries}
    return render(request, 'fond/sousserie/sousserie.html', context)




def add_sousserie(request):
    if request.method=="POST":
        form = Sous_serieForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['sousserie']
            messages.success(request, f"Sous Serie {form_data} ajouter avec succès !")
            return redirect('sousserie')
        else:
            return render(request, 'fond/sousserie/add.html', {"form":form})
    else:
        form = Sous_serieForm()
        return render(request, 'fond/sousserie/add.html', {"form":form})
    
    


def edit_sousserie(request, id):
    sousserie = Sous_serie.objects.get(id=id)
    if request.method == 'POST':
        form = Sous_serieForm(request.POST, instance=sousserie)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Sous Serie {sousserie} modifiéé avec succès !")
            return redirect('sousserie')
    else:
        form = Sous_serieForm(instance=sousserie)
    return render(request, 'fond/sousserie/edit.html',  {'form':form})




def delete_sousserie(request, id):
    sousserie = Sous_serie.objects.get(id = id)
    if request.method=='POST':
        sousserie.delete()
        messages.success(request, f'Sous Serie {sousserie} supprimer avec susccès !')
        return redirect("sousserie")
    return render(request, 'fond/sousserie/delete.html', {"sousserie":sousserie})



def soussousserie(request):
    soussousseries = Sous_sous_Serie.objects.all()
    context = {'soussousseries':soussousseries}
    return render(request, 'fond/soussousserie/soussousserie.html', context)




def add_soussousserie(request):
    if request.method=="POST":
        form = Sous_sous_SerieForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['soussousserie']
            messages.success(request, f"Sous Sous Serie {form_data} ajouter avec succès !")
            return redirect('soussousserie')
        else:
            return render(request, 'fond/soussousserie/add.html', {"form":form})
    else:
        form = Sous_sous_SerieForm()
        return render(request, 'fond/soussousserie/add.html', {"form":form})
    
    


def edit_soussousserie(request, id):
    soussousserie = Sous_sous_Serie.objects.get(id=id)
    if request.method == 'POST':
        form = Sous_sous_SerieForm(request.POST, instance=soussousserie)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Sous Sous Serie {soussousserie} modifiéé avec succès !")
            return redirect('soussousserie')
    else:
        form = Sous_sous_SerieForm(instance=soussousserie)
    return render(request, 'fond/soussousserie/edit.html',  {'form':form})




def delete_soussousserie(request, id):
    soussousserie = Sous_sous_Serie.objects.get(id = id)
    if request.method=='POST':
        soussousserie.delete()
        messages.success(request, f'Sous Sous Serie {soussousserie} supprimer avec susccès !')
        return redirect("soussousserie")
    return render(request, 'fond/soussousserie/delete.html', {"soussousserie":soussousserie})
