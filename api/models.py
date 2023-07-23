from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note (models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]
    


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100, null=True)
    password2 = models.CharField(max_length=100, null=True)
    #email = models.EmailField(max_length=40, null=True)
    #first_name = models.CharField(max_length=40, null=True)
    #last_name = models.CharField(max_length=40, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'