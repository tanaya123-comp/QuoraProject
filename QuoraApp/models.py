from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address=models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField( null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    askedBy=models.ForeignKey(Member,null=True,on_delete=models.SET_NULL)
    tag=models.ForeignKey(Tag,null=True,on_delete=models.SET_NULL)
    description=models.TextField()
    creationTime=models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    question=models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    tag=models.ForeignKey(Tag,null=True,on_delete=models.SET_NULL)
    answer=models.TextField()
    answeredBy=models.ForeignKey(Member,null=True,on_delete=models.SET_NULL)
    creationTime=models.DateTimeField(auto_now_add=True)
    
    
class Vote(models.Model):
    answer=models.ForeignKey(Answer,null=True,on_delete=models.SET_NULL)
    vote=models.IntegerField()#0 -no vote 1-up vote 2-down vote
    votedBy=models.ForeignKey(Member,null=True,on_delete=models.SET_NULL)
    
    
    
    
    




