from django.db import models
from datetime import datetime

class Project(models.Model):
    projectName = models.CharField(max_length=100, default="No title")
    shortDescription = models.TextField(max_length=300, default="No short description")
    longDescription = models.TextField(max_length=300, default="No short description")
    date = models.DateField(default=datetime.now)
    link = models.CharField(max_length=100, default="No link given")
    pic1 = models.CharField(max_length=100, default="No image")
    pic1Description = models.CharField(max_length=100, default="Description of picture")
    pic2 = models.CharField(max_length=100, default="No image")
    pic2Description = models.CharField(max_length=100, default="Description of picture")
    pic3 = models.CharField(max_length=100, default="No image")
    pic3Description = models.CharField(max_length=100, default="Description of picture")