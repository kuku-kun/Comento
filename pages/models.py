from django.db import models

# Create your models here.
class Question(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=200)
    message = models.TextField()
    pub_date = models.DateTimeField('date published')

class Goods(models.Model):
    Kind = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    explain = models.TextField()


