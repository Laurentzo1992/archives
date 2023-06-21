from multiprocessing import context
from django.shortcuts import render, redirect
from urllib import request, response
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.contrib.auth import  login, logout, authenticate, get_user_model
from django.contrib.auth.models import Group, Permission
from  django.contrib import messages
from authentication.models import User
from django.core.paginator import Paginator
from  . import forms
User = get_user_model()
from django.contrib.auth.decorators import login_required #Login required
from  django.views.decorators.cache import cache_control # Destroy the section 
from num2words import num2words


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def statistique(request):
    #AfficRécupéré le nombre des éléments 
    """ cl = Client.objects.count()
    ml = ModelTenue.objects.count()
    tn = Tenue.objects.count()
    cm = Command.objects.count()
    montant_en_lettres = num2words(21, lang='fr') """

    #recupérez les date selectionnées depuis le template
    """    date_depart = request.GET.get('date_depart')
    date_arrive = request.GET.get('date_arrive')
    #Verifie si les dates ont été bien récupéré
    if date_depart and date_arrive:
        #on fait le filtre
        etats1 = Command.objects.filter(date_commande__range=[date_depart, date_arrive]).values('client__telephone', 'client__nom', 'client__prenom').annotate(total=Count('client'))
        etats = LigneCommande.objects.filter(commande__in=Command.objects.all(), commande__date_commande__range=[date_depart, date_arrive]).values('article__libelle').annotate(total=Count('article'), quantite=Sum('quantite'))
    else:
        # si non retourne les éléments sans filtre
        etats1 = Command.objects.all().values('client__telephone', 'client__nom', 'client__prenom').annotate(total=Count('client'))
        etats = LigneCommande.objects.filter(commande__in=Command.objects.all()).values('article__libelle').annotate(total=Count('article'), quantite=Sum('quantite'))
    # on compte le nombre de ligne retournées pour dynamiser le graphique
    barres = etats.count()
    barres1 = etats1.count()
    # on selectionne et on compte le nombre de produit disponible dans la base
    articles = Tenue.objects.all().count()
    # on selectionne et on compte le nombre de commande passées disponible dans la base
    articles_commandes = Command.objects.all().count()
    # on selectionne et on compte le nombre de commande livré disponible dans la base
    articles_livres = Livraison.objects.filter(status=True).count()
    """
    #context={"montant_en_lettres":montant_en_lettres, "cl":cl, "ml":ml, "tn":tn, "cm":cm, "date_depart":date_depart, "date_arrive":date_arrive, "barres1":barres1, "etats1":etats1, "barres":barres, "etats":etats, "articles":articles, "articles_commandes":articles_commandes, "articles_livres":articles_livres}
    context={}
    # on reinitialise le filtre
    #if 'reset' in request.GET:
        #return redirect('statistique') 
    return render(request, 'authentication/statistique/statistique.html', context)



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    if request.user == None or request.user =="" or request.user.username == "":
        return render(request, "authentication/home/login.html")
    else:
        return HttpResponseRedirect('/')
    
#Login User
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user != None:
            login(request, user)
            messages.info(request, "Connexion reussie !")
            return redirect('statistique')
        else:
            messages.error(request, "Veuillez réssayer encore et saisir vos informations de connexion: utilisateur et mot de passe correctement.")
            return HttpResponseRedirect('/')

#Deconnxion
def Logout_user(request):
    logout(request)
    request.user = None
    messages.warning(request, "Deconnexion reussie !")
    return HttpResponseRedirect('/')

# Page d'acceuil 

def home(request):
    """ tenues = Tenue.objects.all().order_by('-id')
    paginator = Paginator(tenues, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) """
    context = {}
    return render(request, 'authentication/home/home.html', context)

@login_required
def delete(request,user_id):
    citoyen = User.objects.get(id = user_id)
    citoyen.delete()
    messages.success(request, 'User deleted successfully !')
    return HttpResponseRedirect("users")
    
#List user  function
def users(request):
    user_lists = User.objects.all()
    return render(request, "authentication/user/user.html", {"user_lists":user_lists})

#User  profile function
""" def profile(request):
    context = {}
    return render(request, "authentication/profile.html", context)

 """


#Function to create users
# def add_user(request):
#     form = forms.CreateUser()
#     if request.method == 'POST':
#         form = forms.CreateUser(request.POST,request.FILES,)
#         if form.is_valid():
#             form.save()
#             return redirect('list')
#     return render(request, 'authentication/add.html', context={'form':form})

# Edit user edit function
# def edit_user(request, id):
#     user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = forms.CreateUser(request.POST,request.FILES, instance=user)
#         if form.is_valid():
#             form.save(id)
#             return redirect('list')
#     else:
#         form = forms.CreateUser(instance=user)
#     return render(request, 'authentication/edit.html', {'form':form})



# def delete_user(request,id):
#     user = User.objects.get(id=id)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('list')
#     return render(request, 'authentication/delete.html', {'user':user})

#----------

