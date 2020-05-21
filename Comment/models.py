from django.db import models

class Comment(models.Model):
    name = models.CharField(max_length=30, default = "Anonymous")
    text = models.TextField(max_length=300, default = "No comment")
