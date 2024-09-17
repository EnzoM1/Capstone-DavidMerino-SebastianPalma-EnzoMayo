from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    return render(request, 'index.html')
