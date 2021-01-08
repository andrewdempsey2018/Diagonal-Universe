from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm
from Comment.models import Comment
from Comment.forms import CommentForm

def index(request):
    latestPost = Post.objects.latest('id')
    categorys = Post.CATEGORYS

    #remove 'projects' from categorys as we dont want this listed on main page
    new = list(categorys)
    new.remove(('Projects', 'Projects'))
    #print("!")
    categorys = tuple(new)
    #print(new)
    
    #get comments unique to the latest post
    comments = Comment.objects.all().filter(subject=latestPost.slug)

    form = CommentForm()

    if request.method == 'POST':
        #if form.is_valid():
        comment = Comment()
        comment.name = request.POST.get('name')
        comment.text = request.POST.get('text')
        comment.subject = latestPost.slug
        comment.save()
        return render(request, 'post/thanks.html')  
    else:
        return render(request, "post/index.html", {'latestPost': latestPost, 'categorys': categorys, 'comments': comments, 'form': form})

def thanks(request):
    return render(request, "post/thanks.html")

def post_list(request, cat):
    postList = Post.objects.filter(category = cat)
    return render(request, "post/post_list.html", {'postList': postList})

def project_list(request):
    postList = Post.objects.filter(category = 'Projects')
    return render(request, "post/post_list.html", {'postList': postList})

#def old_post(request, slug):
#    postToView = Post.objects.get(slug=slug)
#    return render(request, "post/old_post.html", {'postToView': postToView})

def old_post(request, slug):
    #messy code here (entire view should be refactored)
    #old_post view and index view should be the same function
    latestPost = Post.objects.get(slug=slug)
    categorys = Post.CATEGORYS

    #remove 'projects' from categorys as we dont want this listed on main page
    new = list(categorys)
    new.remove(('Projects', 'Projects'))
    print("!")
    categorys = tuple(new)
    print(new)
    
    #get comments unique to the latest post
    comments = Comment.objects.all().filter(subject=latestPost.slug)

    form = CommentForm()

    if request.method == 'POST':
        #if form.is_valid():
        comment = Comment()
        comment.name = request.POST.get('name')
        comment.text = request.POST.get('text')
        comment.subject = latestPost.slug
        comment.save()
        return render(request, 'post/thanks.html')  
    else:
        return render(request, "post/index.html", {'latestPost': latestPost, 'categorys': categorys, 'comments': comments, 'form': form})

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = PostForm()
    return render(request, "post/new_post.html", {'form': form})
