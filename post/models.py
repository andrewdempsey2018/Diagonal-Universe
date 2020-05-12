from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.TextField(max_length=300)
    category = models.CharField(max_length=20)
    date = models.DateField()
    text = models.TextField(max_length=3000)
    # comments
    topPicphoto = models.CharField(max_length=100)
    topPicphotoDescription = models.CharField(max_length=100, default="Description of picture")

    middlePicphoto = models.CharField(max_length=100)
    middlePicphotoDescription = models.CharField(max_length=300, default="Description of picture")

    youtube = models.CharField(max_length=100, default="No video for this post")
    github = models.CharField(max_length=100, default="No repo for this post")