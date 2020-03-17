from django.shortcuts import render
from django.http import HttpResponse

# Import the Story model for use
from .models import Post

def index(request):
    return render(request, "index.html")
