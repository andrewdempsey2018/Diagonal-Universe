from django.db import models
from datetime import datetime

class Post(models.Model):

    TECH = 'Tech'
    TUTORIALS = 'Tutorials'
    PROJECTS = 'Projects'

    CATEGORYS = (
        (TECH, 'Tech'),
        (TUTORIALS, 'Tutorials'),
        (PROJECTS, 'Projects'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default="None")
    subtitle = models.TextField(max_length=300, default="No subtitle")
    category = models.CharField(max_length=20, choices=CATEGORYS, default=TECH)
    date = models.DateField(default=datetime.now)
    
    topImage = models.CharField(max_length=100, default="No image")
    topImageDescription = models.CharField(max_length=100, default="Description of picture")

    text1 = models.TextField(max_length=3000, default="No text")

    middleImage = models.CharField(max_length=100, default="No image")
    middleImageDescription = models.CharField(max_length=300, default="Description of picture")

    text2 = models.TextField(max_length=3000, default="No text")

    extraImage1 = models.CharField(max_length=100, default="No image")
    extraImage1Description = models.CharField(max_length=100, default="Description of picture")

    extraImage2 = models.CharField(max_length=100, default="No image")
    extraImage2Description = models.CharField(max_length=100, default="Description of picture")

    extraImage3 = models.CharField(max_length=100, default="No image")
    extraImage3Description = models.CharField(max_length=100, default="Description of picture")

    video = models.CharField(max_length=100, default="No video for this post")
    repo = models.CharField(max_length=100, default="No repo for this post")

    references = models.TextField(max_length=1000, default="No references")

    # User comments to be coded