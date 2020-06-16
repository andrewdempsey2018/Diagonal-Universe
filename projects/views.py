from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {'projects': projects})

def project_detail(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, "projects/project_detail.html", {'project': project})