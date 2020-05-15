from django.db import models



class Post(models.Model):

    TECH = 'Tech'
    GAMING = 'Gaming'
    COMPUTING = 'Computing'
    POLITICS = 'Politics'
    PHILOSOPHY = 'Philosophy'
    CODERDOJO = 'CoderDojo'
    CULTURE = 'Culture'
    TUTORIALS = 'Tutorials'
    SCIENCE = 'Science'

    CATEGORYS = (
        (TECH, 'Tech'),
        (GAMING, 'Gaming'),
        (COMPUTING, 'Computing'),
        (POLITICS, 'Politics'),
        (PHILOSOPHY, 'Philosophy'),
        (CODERDOJO, 'CoderDojo'),
        (CULTURE, 'Culture'),
        (TUTORIALS, 'Tutorials'),
        (SCIENCE, 'Science'),
    )

    title = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=300)
    category = models.CharField(max_length=20, choices=CATEGORYS, default=TECH)
    date = models.DateField()
    
    topImage = models.CharField(max_length=100)
    topImageDescription = models.CharField(max_length=100, default="Description of picture")

    text1 = models.TextField(max_length=3000, default="No text")

    middleImage = models.CharField(max_length=100)
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

    references = models.TextField(max_length=1000, default="none")

    # User comments to be coded