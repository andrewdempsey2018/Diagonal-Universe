from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from Comment.models import Comment

def index(request):
    latestPost = Post.objects.latest('id')
    categorys = Post.CATEGORYS
    comments = Comment.objects.all()
    return render(request, "post/index.html", {'latestPost': latestPost, 'categorys': categorys, 'comments': comments})