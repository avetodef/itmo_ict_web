from django.db import models
class Feedback(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.CharField(max_length=2)
    email = models.CharField(max_length=20)
    comment = models.CharField(max_length=100)
# Create your models here.
