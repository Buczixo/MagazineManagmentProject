from django.shortcuts import render

# Create your views here.
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


