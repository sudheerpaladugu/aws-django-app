from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("You are web app is running")

def register_email(request):
    return render(request, 'index.html')
