from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    address=models.CharField(max_length=200,null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True, default='default_profile.png')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, null=True)


    def __str__(self):
        return self.name

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,null=True)
    description=models.CharField(max_length=200,null=True)
    tag_pic = models.ImageField(upload_to='tags/', null=True, blank=True, default='default_tag.png')

    def __str__(self):
        return self.name

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    askedBy=models.ForeignKey(Member,null=True, blank=True, on_delete=models.SET_NULL)
    tag=models.ForeignKey(Tag,null=True,on_delete=models.SET_NULL)
    description=models.CharField(max_length=500)
    creationTime=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description




class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question=models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    tag=models.ForeignKey(Tag,null=True,on_delete=models.SET_NULL)
    answer=RichTextField(blank=True,null=True)
    answeredBy=models.ForeignKey(Member,null=True,on_delete=models.SET_NULL)
    creationTime=models.DateTimeField(auto_now_add=True)

    class Meta:
        order_with_respect_to = 'question'
    
    
class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    answer=models.ForeignKey(Answer,null=True,on_delete=models.CASCADE)
    vote=models.IntegerField()# 1-up vote 2-down vote 0-no vote
    votedBy=models.ForeignKey(Member,null=True,on_delete=models.CASCADE)

class Employee(models.Model):
    member=models.ForeignKey(Member, on_delete=models.CASCADE)
    company=models.CharField(max_length=200, null=True, blank=True)
    job_post=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.member.name

class Student(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    university = models.CharField(max_length=200, null=True, blank=True)
    degree = models.CharField(max_length=200, null=True, blank=True)
    branch = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.member.name

class Following(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    
    
    
    
    




