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


# Create your views here.

def rejestracja(request):
    if request.user.is_authenticated :
        return redirect('glowna')
    else :
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

    return render(request, 'rejestracja.html', context)


@login_required(login_url='logowanie')
def main(request):
    return render(request, 'index.html')


def logowanie(request):
    if request.user.is_authenticated :
        return redirect('home')
    else :
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
def odbior(request):
    return render(request, 'odbior.html')


@login_required(login_url='logowanie')
def wydanie(request):
    return render(request, 'wydanie.html')


@login_required(login_url='logowanie')
def przerzucenie(request):
    return render(request, 'przerzucenie.html')


@login_required(login_url='logowanie')
def u_magazynu(request):
    return render(request, 'u_magazynu.html')


@login_required(login_url='logowanie')
def w_magazynu(request):
    return render(request, 'w_magazynu.html')


@login_required(login_url='logowanie')
def wyszukanie(request):
    return render(request, 'wyszukanie.html')


@login_required(login_url='logowanie')
def b_towarow(request):
    return render(request, 'b_towarow.html')


@login_required(login_url='logowanie')
def b_dostawcow(request):
    return render(request, 'b_dostawcow.html')


@login_required(login_url='logowanie')
def b_pracownikow(request):
    return render(request, 'b_pracownikow.html')
