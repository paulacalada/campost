from django.shortcuts import render
from .forms import ClientRegistration, ClientStore, CompteGestion
from .models import User, Client, Compte

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = ClientRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            tl = fm.cleaned_data['telephone']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, telephone = tl, email = em, password = pw)
            reg.save()
            fm = ClientRegistration()
    else:
        fm = ClientRegistration()
    return render(request, 'client/addandshow.html',{'form':fm})

def add_show_client(request):
    if request.method == 'POST':
        fm = ClientStore(request.POST)
        if fm.is_valid():
            nom = fm.cleaned_data['nom']
            pren = fm.cleaned_data['prenom']
            tel = fm.cleaned_data['telephone']
            adr = fm.cleaned_data['adresse']
            reg = Client(nom = nom, prenom = pren, telephone =tel , adresse = adr)
            reg.save()
            fm = ClientStore()
    else:
        fm = ClientStore()
    return render(request, 'Clients/edit.html',{'form':fm})

def traiter_compte(request):
    if request.method == 'POST':
        fm = CompteGestion(request.POST)
        if fm.is_valid():
            num = fm.cleaned_data['numero']
            cli = fm.cleaned_data['client']
            solde = fm.cleaned_data['solde']
            jr = fm.cleaned_data['jour']
            cpt = Compte(numero = num, client = cli, solde =solde , jour = jr)
            cpt.save()
            fm = CompteGestion()
    else:
        fm = CompteGestion()
    return render(request, 'Comptes/edit.html',{'form':fm})