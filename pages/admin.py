from django.contrib import admin
from .models import Question
from .models import Goods
# Register your models here.

admin.site.register(Goods)
admin.site.register(Question)