from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
# Primero se debe de crear un archivo urls.py dentro de la app, para poder indicar como va a acceder a la vista que estamos creando

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/base.html", {"name":ls.name})

def home(response):
    return render(response, "main/home.html", {"name":"test"})