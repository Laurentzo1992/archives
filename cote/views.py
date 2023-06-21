from django.shortcuts import render
from cote.models import *
from  django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from cote.forms import *
from django.contrib.auth.decorators import login_required, permission_required
from  django.views.decorators.cache import cache_control 
from datetime import date, datetime
from django.db import transaction, models
from django.db.models import Count, Sum



def site(request):
    sites = Site.objects.all()
    context = {'sites':sites}
    return render(request, 'cote/site/site.html', context)




def add_site(request):
    if request.method=="POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['site']
            messages.success(request, f"Site {form_data} ajouter avec succès !")
            return redirect('site')
        else:
            return render(request, 'cote/site/add.html', {"form":form})
    else:
        form = SiteForm()
        return render(request, 'cote/site/add.html', {"form":form})
    
    


def edit_site(request, id):
    site = Site.objects.get(id=id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Site {site} modifiéé avec succès !")
            return redirect('site')
    else:
        form = SiteForm(instance=site)
    return render(request, 'cote/site/edit.html',  {'form':form})




def delete_site(request, id):
    site = Site.objects.get(id = id)
    if request.method=='POST':
        site.delete()
        messages.success(request, f'Site {site} supprimer avec susccès !')
        return redirect("site")
    return render(request, 'cote/site/delete.html', {"site":site})






def salle(request):
    salles = Salle.objects.all()
    context = {'salles':salles}
    return render(request, 'cote/salle/salle.html', context)




def add_salle(request):
    if request.method=="POST":
        form = SalleForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['salle']
            messages.success(request, f"Salle {form_data} ajouter avec succès !")
            return redirect('salle')
        else:
            return render(request, 'cote/salle/add.html', {"form":form})
    else:
        form = SalleForm()
        return render(request, 'cote/salle/add.html', {"form":form})
    
    


def edit_salle(request, id):
    salle = Salle.objects.get(id=id)
    if request.method == 'POST':
        form = SalleForm(request.POST, instance=salle)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Salle {salle} modifiéé avec succès !")
            return redirect('salle')
    else:
        form = SalleForm(instance=salle)
    return render(request, 'cote/salle/edit.html',  {'form':form})




def delete_salle(request, id):
    salle = Salle.objects.get(id = id)
    if request.method=='POST':
        salle.delete()
        messages.success(request, f'Salle {salle} supprimer avec susccès !')
        return redirect("salle")
    return render(request, 'cote/salle/delete.html', {"salle":salle})





def travee(request):
    travees = Travee.objects.all()
    context = {'travees':travees}
    return render(request, 'cote/travee/travee.html', context)




def add_travee(request):
    if request.method=="POST":
        form = TraveeForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['travee']
            messages.success(request, f"Travée {form_data} ajouter avec succès !")
            return redirect('travee')
        else:
            return render(request, 'cote/travee/add.html', {"form":form})
    else:
        form = TraveeForm()
        return render(request, 'cote/travee/add.html', {"form":form})
    
    


def edit_travee(request, id):
    travee = Travee.objects.get(id=id)
    if request.method == 'POST':
        form = TraveeForm(request.POST, instance=travee)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Travée {travee} modifiéé avec succès !")
            return redirect('travee')
    else:
        form = TraveeForm(instance=travee)
    return render(request, 'cote/travee/edit.html',  {'form':form})




def delete_travee(request, id):
    travee = Travee.objects.get(id = id)
    if request.method=='POST':
        travee.delete()
        messages.success(request, f'Travée {travee} supprimer avec susccès !')
        return redirect("travee")
    return render(request, 'cote/travee/delete.html', {"travee":travee})




def rayon(request):
    rayons = Rayon.objects.all()
    context = {'rayons':rayons}
    return render(request, 'cote/rayon/rayon.html', context)




def add_rayon(request):
    if request.method=="POST":
        form = RayonForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['rayon']
            messages.success(request, f"Rayon {form_data} ajouter avec succès !")
            return redirect('rayon')
        else:
            return render(request, 'cote/rayon/add.html', {"form":form})
    else:
        form = RayonForm()
        return render(request, 'cote/rayon/add.html', {"form":form})
    
    


def edit_rayon(request, id):
    rayon = Rayon.objects.get(id=id)
    if request.method == 'POST':
        form = RayonForm(request.POST, instance=rayon)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Rayon {rayon} modifiéé avec succès !")
            return redirect('rayon')
    else:
        form = RayonForm(instance=rayon)
    return render(request, 'cote/rayon/edit.html',  {'form':form})




def delete_rayon(request, id):
    rayon = Rayon.objects.get(id = id)
    if request.method=='POST':
        rayon.delete()
        messages.success(request, f'Rayon {rayon} supprimer avec susccès !')
        return redirect("rayon")
    return render(request, 'cote/rayon/delete.html', {"rayon":rayon})




def boite(request):
    boites = Boite.objects.all()
    context = {'boites':boites}
    return render(request, 'cote/boite/boite.html', context)




def add_boite(request):
    if request.method=="POST":
        form = BoiteForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['boite']
            messages.success(request, f"Boite {form_data} ajouter avec succès !")
            return redirect('boite')
        else:
            return render(request, 'cote/boite/add.html', {"form":form})
    else:
        form = BoiteForm()
        return render(request, 'cote/boite/add.html', {"form":form})
    
    


def edit_boite(request, id):
    boite = Boite.objects.get(id=id)
    if request.method == 'POST':
        form = BoiteForm(request.POST, instance=boite)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Boite {boite} modifiéé avec succès !")
            return redirect('boite')
    else:
        form = BoiteForm(instance=boite)
    return render(request, 'cote/boite/edit.html', {'form':form})




def delete_boite(request, id):
    boite = Boite.objects.get(id = id)
    if request.method=='POST':
        boite.delete()
        messages.success(request, f'Boite {boite} supprimer avec susccès !')
        return redirect("boite")
    return render(request, 'cote/boite/delete.html', {"boite":boite})