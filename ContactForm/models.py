from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=30)
    message = models.TextField(max_length=300)

