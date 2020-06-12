from django.shortcuts import render
from django.http import HttpResponse

from .models import Project

def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {'projects': projects})