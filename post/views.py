from django.shortcuts import render
from django.http import HttpResponse

# Import the Story model for use
from .models import Post

def index(request):
    latestPost = Post.objects.latest('id')
    categorys = Post.CATEGORYS
    return render(request, "index.html", {'latestPost': latestPost, 'categorys': categorys})