from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm
from Comment.models import Comment
from Comment.forms import CommentForm

def view_post(request, slug=None):
    if slug is None:
        post = Post.objects.latest('id')
    else:
        post = Post.objects.get(slug=slug)

    # Grab a list of ppost categorys for display in the side panel
    categorys = Post.CATEGORYS
    
    # Get comments unique to the displayed post
    comments = Comment.objects.all().filter(subject=post.slug)

    # Generate a form for user comments
    form = CommentForm()

    if request.method == 'POST':
        comment = Comment()
        comment.name = request.POST.get('name')
        comment.text = request.POST.get('text')
        comment.subject = post.slug
        comment.save()
        return render(request, 'post/thanks.html')
    
    return render(request, "post/view_post.html", {'post': post, 'categorys': categorys, 'comments': comments, 'form': form})

def thanks(request):
    return render(request, "post/thanks.html")

def post_list(request, cat):

    if cat == 'Projects':
        title = "Projectiles yes!!"
    else:
        title = "Listing posts in the category: " + cat

    postList = Post.objects.filter(category = cat)
    return render(request, "post/post_list.html", {'postList': postList, 'title': title})

@login_required(login_url='/admin/')
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render(request, "post/new_post.html", {'form': form})
