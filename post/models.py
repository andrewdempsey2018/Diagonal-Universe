from django.db import models
from datetime import datetime

class Post(models.Model):

    TECH = 'Tech'
    TUTORIALS = 'Tutorials'
    PROJECTS = 'Projects'
    COMPUTING = 'Computing'
    CULTURE = 'Culture'
    THOUGHTS = 'Thoughts'

    CATEGORYS = (
        (TECH, 'Tech'),
        (TUTORIALS, 'Tutorials'),
        (PROJECTS, 'Projects'),
        (COMPUTING, 'Computing'),
        (CULTURE, 'Culture'),
        (THOUGHTS, 'Thoughts'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, default="None")
    subtitle = models.TextField(max_length=300, default="No subtitle")
    category = models.CharField(max_length=20, choices=CATEGORYS, default=TECH)
    date = models.DateField(default=datetime.now)
    
    text1 = models.TextField(max_length=7000, default="No text")

    text2 = models.TextField(max_length=7000, default="No text")

    video = models.CharField(max_length=100, default="No video for this post")

    # User comments to be coded