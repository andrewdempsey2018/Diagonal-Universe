from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=30, default="")
    email = models.EmailField(max_length=254, default="")
    message = models.TextField(max_length=300, default="")

