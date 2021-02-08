from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import F
# Create your models here.

class Question(models.Model):
    qid=models.OneToOneField('auth.User',unique=True,null=False, on_delete=models.CASCADE)
    question=models.CharField(null=False, blank=False,max_length=100)
    
        

class Option(models.Model):
    name=models.CharField(null=False, blank=False,max_length=100)
    link=models.CharField(null=False, blank=False,max_length=100)
    quest=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s" % (self.name, self.link)

class Voter(models.Model):
    email=models.EmailField(null=False,blank=False,max_length=100)
    vname=models.CharField(null=False,blank=False,max_length=50)
    opname=models.CharField(max_length=100)
    vote=models.ForeignKey(Question,on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s" % (self.email, self.vname)

        


 

