from django.shortcuts import render
from paramettre.models import Archive_statuts, Archive_type, Document_type, Provenance
from  django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .forms import Archive_statutsForm, Archive_typeForm, Document_typeForm, ProvenanceForm
from django.contrib.auth.decorators import login_required, permission_required
from  django.views.decorators.cache import cache_control 
from datetime import date, datetime
from django.db import transaction, models
from django.db.models import Count, Sum



def archive_statut(request):
    archive_statuts = Archive_statuts.objects.all()
    context = {'archive_statuts':archive_statuts}
    return render(request, 'paramettre/archive_statut/archive_statut.html', context)




def add_statut(request):
    if request.method=="POST":
        form = Archive_statutsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Status ajouter avec succès !")
            return redirect('archive_statut')
        else:
            return render(request, 'paramettre/archive_statut/add.html', {"form":form})
    else:
        form = Archive_statutsForm()
        return render(request, 'paramettre/archive_statut/add.html', {"form":form})
    
    


def edit_statut(request, id):
    archive_statut = Archive_statuts.objects.get(id=id)
    if request.method == 'POST':
        form = Archive_statutsForm(request.POST, instance=archive_statut)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Status {archive_statut} modifiéé avec succès !")
            return redirect('archive_statut')
    else:
        form = Archive_statutsForm(instance=archive_statut)
    return render(request, 'paramettre/archive_statut/edit.html',  {'form':form})




def delete_statut(request, id):
    archive_statut = Archive_statuts.objects.get(id = id)
    if request.method=='POST':
        archive_statut.delete()
        messages.success(request, f'Status {archive_statut} supprimer avec susccès !')
        return redirect("archive_statut")
    return render(request, 'paramettre/archive_statut/delete.html', {"archive_statut":archive_statut})




def archive_type(request):
    archive_types = Archive_type.objects.all()
    context = {'archive_types':archive_types}
    return render(request, 'paramettre/archive_type/archive_type.html', context)




def add_type(request):
    if request.method=="POST":
        form = Archive_typeForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['libelle']
            messages.success(request, f"Type d'archive {form_data} ajouter avec succès !")
            return redirect('archive_type')
        else:
            return render(request, 'paramettre/archive_type/add.html', {"form":form})
    else:
        form = Archive_typeForm()
        return render(request, 'paramettre/archive_type/add.html', {"form":form})
    
    


def edit_type(request, id):
    archive_type = Archive_type.objects.get(id=id)
    if request.method == 'POST':
        form = Archive_typeForm(request.POST, instance=archive_type)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Type d'archive {archive_type} modifiéé avec succès !")
            return redirect('archive_type')
    else:
        form = Archive_typeForm(instance=archive_type)
    return render(request, 'paramettre/archive_type/edit.html',  {'form':form})




def delete_type(request, id):
    archive_type = Archive_type.objects.get(id = id)
    if request.method=='POST':
        archive_type.delete()
        messages.success(request, f"Type d'archive {archive_type} supprimer avec susccès !")
        return redirect("archive_type")
    return render(request, 'paramettre/archive_type/delete.html', {"archive_type":archive_type})






def document_type(request):
    document_types = Document_type.objects.all()
    context = {'document_types':document_types}
    return render(request, 'paramettre/document_type/document_type.html', context)




def add_document(request):
    if request.method=="POST":
        form = Document_typeForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['libelle']
            messages.success(request, f"Type dcoument {form_data} ajouter avec succès !")
            return redirect('document_type')
        else:
            return render(request, 'paramettre/document_type/add.html', {"form":form})
    else:
        form = Document_typeForm()
        return render(request, 'paramettre/document_type/add.html', {"form":form})
    
    


def edit_document(request, id):
    document_type = Document_type.objects.get(id=id)
    if request.method == 'POST':
        form = Document_typeForm(request.POST, instance=document_type)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Type Document {document_type} modifiéé avec succès !")
            return redirect('document_type')
    else:
        form = Document_typeForm(instance=document_type)
    return render(request, 'paramettre/document_type/edit.html',  {'form':form})




def delete_document(request, id):
    document_type = Document_type.objects.get(id = id)
    if request.method=='POST':
        document_type.delete()
        messages.success(request, f"Type Document {document_type} supprimer avec susccès !")
        return redirect("document_type")
    return render(request, 'paramettre/document_type/delete.html', {"document_type":document_type})





def provenance(request):
    provenances = Provenance.objects.all()
    context = {'provenances':provenances}
    return render(request, 'paramettre/provenance/provenance.html', context)




def add_provenance(request):
    if request.method=="POST":
        form = ProvenanceForm(request.POST)
        if form.is_valid():
            form.save()
            form_data = form.cleaned_data['sigle']
            messages.success(request, f"Direction {form_data} ajouter avec succès !")
            return redirect('provenance')
        else:
            return render(request, 'paramettre/provenance/add.html', {"form":form})
    else:
        form = ProvenanceForm()
        return render(request, 'paramettre/provenance/add.html', {"form":form})
    
    


def edit_provenance(request, id):
    provenance = Provenance.objects.get(id=id)
    if request.method == 'POST':
        form = ProvenanceForm(request.POST, instance=provenance)
        if form.is_valid():
            form.save(id)
            messages.success(request, f"Direction {provenance} modifiéé avec succès !")
            return redirect('provenance')
    else:
        form = ProvenanceForm(instance=provenance)
    return render(request, 'paramettre/provenance/edit.html',  {'form':form})




def delete_provenance(request, id):
    provenance = Provenance.objects.get(id = id)
    if request.method=='POST':
        document_type.delete()
        messages.success(request, f"Direction {provenance} supprimer avec susccès !")
        return redirect("provenance")
    return render(request, 'paramettre/provenance/delete.html', {"provenance":provenance})