from django.db import models
from django import forms
# Create your models here.
class Todo(models.Model):
    details = models.TextField()
    status= models.BooleanField(default=False)

