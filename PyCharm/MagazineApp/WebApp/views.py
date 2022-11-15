# sqlite https://www.sqlitetutorial.net

from django.shortcuts import render

# import formy kreacji użytkownika, tutorial
# https://www.youtube.com/watch?v=tUqUdu0Sjyc
from django.contrib.auth.forms import UserCreationForm
#import zmienionego formularza
from templates.forms import ForDodPrac

# Create your views here.

def rejestracja(request):
    form = ForDodPrac()
    context = {'form':form}
    # Zapis danych z formularza jeśli formularz jest poprawny oraz auto hashowanie hasła
    if request.method == 'POST':
        form = ForDodPrac(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'rejestracja.html', context)
def main(request):
    return render(request, 'index.html')
def logowanie(request):
    return render(request, 'logowanie.html')

def odbior(request) :
    return render(request, 'odbior.html')

def wydanie(request) :
    return render(request, 'wydanie.html')

def przerzucenie(request) :
    return render(request, 'przerzucenie.html')

def u_magazynu(request) :
    return render(request, 'u_magazynu.html')

def w_magazynu(request) :
    return render(request, 'w_magazynu.html')

def wyszukanie(request) :
    return render(request, 'wyszukanie.html')

def b_towarow(request) :
    return render(request, 'b_towarow.html')

def b_dostawcow(request) :
    return render(request, 'b_dostawcow.html')

def b_pracownikow(request) :
    return render(request, 'b_pracownikow.html')


