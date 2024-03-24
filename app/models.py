from django.db import models

# Create your models here.

class Note(models.Model):
    Notes = models.CharField(max_length=255)
