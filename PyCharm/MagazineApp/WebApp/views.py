from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'index.html')
def logowanie(request):
    return render(request, 'logowanie.html')

