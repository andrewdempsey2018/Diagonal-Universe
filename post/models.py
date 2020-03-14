from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    category = models.CharField(max_length=20)
    date = models.DateField()
    text = models.CharField(max_length=3000)
    # comments
    topPicphoto = models.ImageField(upload_to="cars")
    middlePicphoto = models.ImageField(upload_to="cars")
    middlePicDescription = models.CharField(max_length=300)
