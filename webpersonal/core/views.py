from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Mi web</h1> <h2>jrm2087</h2>')
