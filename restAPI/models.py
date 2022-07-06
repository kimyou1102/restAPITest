from turtle import update
from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)