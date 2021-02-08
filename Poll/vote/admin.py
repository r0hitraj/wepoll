from django.contrib import admin
from django.contrib.auth.models import User
from .models import Question,Option,Voter
# Register your models here.

admin.site.register(Question) #here parameter is model class of Question 

admin.site.register(Option) #here parameter is modal class of Option Table
admin.site.register(Voter)