from django.db import models

# Create your models here. - DB 생성
class MainContent(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
