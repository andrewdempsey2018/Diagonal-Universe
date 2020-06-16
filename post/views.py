from django.shortcuts import render
from django.http import HttpResponse

from .models import Post
from Comment.models import Comment
from Comment.forms import CommentForm

def index(request):
    latestPost = Post.objects.latest('id')
    categorys = Post.CATEGORYS
    comments = Comment.objects.all()
    form = CommentForm()

    if request.method == 'POST':
        #if form.is_valid():
        comment = Comment()
        comment.name = request.POST.get('name')
        comment.text = request.POST.get('text')
        comment.save()
        return render(request, 'post/thanks.html')  
    else:
        return render(request, "post/index.html", {'latestPost': latestPost, 'categorys': categorys, 'comments': comments, 'form': form})

def thanks(request):
    return render(request, "post/thanks.html")

def post_list(request, cat):
    postList = Post.objects.filter(category = cat)
    return render(request, "post/post_list.html", {'postList': postList})

def old_post(request, slug):
    postToView = Post.objects.get(slug=slug)
    return render(request, "post/old_post.html", {'postToView': postToView})
