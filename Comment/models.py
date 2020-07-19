from django.db import models

class Comment(models.Model):
    subject = models.SlugField(max_length=100, default="None") #subject of comment is the slug of the post in question
    name = models.CharField(max_length=30, default = "Anonymous")
    text = models.TextField(max_length=300, default = "No comment")