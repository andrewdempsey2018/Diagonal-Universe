from django.shortcuts import render
from django.http import HttpResponse

#from .models import Post

def projects(request):
    return render(request, "projects/projects.html")