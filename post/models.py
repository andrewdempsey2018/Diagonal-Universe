from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=300)
    category = models.CharField(max_length=20)
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

    # User comments to be coded