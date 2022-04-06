from django.db import models
#from django.conf import settings


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

class articles(models.Model):
    title = models.CharField(max_length=200,db_index=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.IntegerField()
    write = models.TextField(default='null')
    email = models.TextField(default='null')

    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class comment(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.IntegerField()
    write = models.TextField(default='null')



