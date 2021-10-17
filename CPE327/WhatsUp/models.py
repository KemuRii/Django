from django.db import models

class User_Name(models.Model):
    User_ID=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)

class Chat_Room(models.Model):
    Room_name=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)