from django.shortcuts import render
from django.http import HttpResponse

from .models import Post

def index(request):
    latestPost = Post.objects.latest('id')
    categorys = Post.CATEGORYS
    return render(request, "post/index.html", {'latestPost': latestPost, 'categorys': categorys})