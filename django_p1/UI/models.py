from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    marital = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pics')
