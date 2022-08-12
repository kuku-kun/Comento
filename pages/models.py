from django.db import models

# Create your models here.
class Question(models.Model):
    FullName = models.CharField(max_length=200)
    Email = models.EmailField()
    PhoneNumber = models.CharField(max_length=200)
    Message = models.TextField()
    pub_date = models.DateTimeField('date published')
