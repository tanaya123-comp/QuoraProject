from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address=models.CharField(max_length=200,null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True, default='default_profile.png')
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
    answer=HTMLField()
    answeredBy=models.ForeignKey(Member,null=True,on_delete=models.SET_NULL)
    creationTime=models.DateTimeField(auto_now_add=True)
    
    
class Vote(models.Model):
    answer=models.ForeignKey(Answer,null=True,on_delete=models.SET_NULL)
    vote=models.IntegerField()#0 -no vote 1-up vote 2-down vote
    votedBy=models.ForeignKey(Member,null=True,on_delete=models.SET_NULL)

class Employee(models.Model):
    member=models.ForeignKey(Member, on_delete=models.CASCADE)
    company=models.CharField(max_length=200, null=True, blank=True)
    job_post=models.CharField(max_length=200, null=True, blank=True)

class Student(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    university = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    branch = models.CharField(max_length=200, null=True, blank=True)

class Following(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    
    
    
    
    




