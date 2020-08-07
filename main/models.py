from django.db import models

from datetime import date
from datetime import datetime


class Manager(models.Manager):  #importing models module ..creating manager class`
    def basic_validator(self, postData):
        errors = {}
        
        # add keys and values to errors dictionary
        if len(postData['titleLabel']) <2:
            errors['titleLabel'] = "Movie title must be more than 2 characters"
        if len(postData['networkLabel']) <2:
            errors['networkLabel'] = "Network must be more than 2 characters"
        if len(postData['releaseDateLabel']) < 10:
            errors['releaseDateLabel'] = "release date must be entered"
        elif datetime.strptime(postData['releaseDateLabel'], '%Y-%m-%d') > datetime.now():
            errors['releaseDateLabel'] = "need current date"
        if len(postData['descriptionLabel']) <10:
            errors['descriptionLabel'] = "The description must be at least 10 characters"
        return errors

# Create your models here.
class Show(models.Model): #created a new class show. inherting from class (object)
    #creating a class attribute called title 
    #assigning a new instance of the CharField class
    title = models.CharField(max_length=64) 
    network = models.CharField(max_length=64)
    release_date = models.DateField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #creating a class attribute called objects
    #assigning it to new instance of the MovieManage Class
    objects = Manager() 



class User (models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=64)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)