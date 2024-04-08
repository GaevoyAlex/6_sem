from django.db import models

# Create your models here.

class Creator (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class User (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Event (models.Model):
    title = models.CharField(max_length=100) 
    description = models.CharField(max_length=400)
    date = models.CharField(max_length=20)

    likes = models.IntegerField()


    

        