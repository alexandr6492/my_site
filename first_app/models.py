from email import message
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import User

UserModel = get_user_model()

class Topic(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=255)
    users = models.ManyToManyField(UserModel, through='UserTopicRelationship')

    def str(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255, default='default_title')
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE,  null=True)
    topics = models.ManyToManyField(Topic)

    def str(self):
        return self.title

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author= models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def str(self):
        return f"Comment by {self.author.username} on {self.article.title}"
    
class UserTopicRelationship(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    notify = models.BooleanField(default=False)

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_tags = models.ManyToManyField(Article)












    

