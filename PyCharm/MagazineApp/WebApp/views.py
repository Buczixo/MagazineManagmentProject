# sqlite https://www.sqlitetutorial.net

from django.shortcuts import render, redirect
from django.contrib import messages
# import formy kreacji użytkownika, tutorial
# https://www.youtube.com/watch?v=tUqUdu0Sjyc
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# import zmienionego formularza
from templates.forms import ForDodPrac

# import biblioteki restrykcji otwierania
from django.contrib.auth.decorators import login_required

# import dla modeli i ich formsów
from .forms import MagazynForm, OpakowanieForm, ProduktForm, DocumentForm
from .models import Opakowanie, Produkt, Magazyn, Dokument

# https://stackoverflow.com/questions/23139657/django-get-all-users
from django.contrib.auth import get_user_model


# Create your views here.

def rejestracja(request):
    if request.user.is_superuser:
        form = ForDodPrac()
        context = {'form': form}
        # Zapis danych z formularza jeśli formularz jest poprawny oraz auto hashowanie hasła
        if request.method == 'POST':
            form = ForDodPrac(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Użytkownik %s utworzony poprawnie' % user)
                return redirect('logowanie')

    else:
        return redirect('home')

    return render(request, 'rejestracja.html', context)


@login_required(login_url='logowanie')
def home(request):
    return render(request, 'index.html')


def logowanie(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Hasło albo login niepoprawne !")

        context = {}
        return render(request, 'logowanie.html')


@login_required(login_url='logowanie')
def wylogowanie(request):
    logout(request)
    return redirect('logowanie')


@login_required(login_url='logowanie')
def dostawa(request):
    data = Dokument.objects.filter(typ = 'Dostawa')
    return render(request, 'dostawa.html', {'data': data})


@login_required(login_url='logowanie')
def wydanie(request):
    data = Dokument.objects.filter(typ = 'Wydanie')
    return render(request, 'wydanie.html', {'data': data})


@login_required(login_url='logowanie')
def u_dokumentu(request):
    form = DocumentForm()
    context = {'form': form}
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'u_dokumentu.html', context)

@login_required(login_url='logowanie')
def przerzucenie(request):
    return render(request, 'przerzucenie.html')


@login_required(login_url='logowanie')
def u_magazynu(request):
    form = MagazynForm()
    context = {'form': form}
    if request.method == 'POST':
        form = MagazynForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'u_magazynu.html', context)


@login_required(login_url='logowanie')
def u_towaru(request):
    form = ProduktForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProduktForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'u_towarow.html', context)


# def rejestracja(request):
#     if request.user.is_authenticated :
#         return redirect('glowna')
#     else :
#         form = ForDodPrac()
#         context = {'form': form}
#         # Zapis danych z formularza jeśli formularz jest poprawny oraz auto hashowanie hasła
#         if request.method == 'POST':
#             form = ForDodPrac(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Użytkownik %s utworzony poprawnie' % user)
#                 return redirect('logowanie')
#
#     return render(request, 'rejestracja.html', context)



@login_required(login_url='logowanie')
def w_magazynu(request):
    data = Magazyn.objects.all()
    return render(request, 'w_magazynu.html', {'data': data})


@login_required(login_url='logowanie')
def wyszukanie(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Produkt.objects.filter(nazwaProduktu__contains=q)
    else :
        data = Produkt.objects.all()
    return render(request, 'wyszukanie.html', {'data': data})


@login_required(login_url='logowanie')
def b_towarow(request):
    data = Produkt.objects.all()
    return render(request, 'b_towarow.html', {'data': data})


@login_required(login_url='logowanie')
def b_dostawcow(request):
    User = get_user_model()
    data = User.objects.all()
    return render(request, 'b_dostawcow.html', {'data': data})


@login_required(login_url='logowanie')
def b_pracownikow(request):
    User = get_user_model()
    data = User.objects.all()
    return render(request, 'b_pracownikow.html', {'data': data})
