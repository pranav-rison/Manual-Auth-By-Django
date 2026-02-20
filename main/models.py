from django.db import models

# Create your models here.

# 1st for regiser page 
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    # unique=True ensures that no two users can have the same email address
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    conform_password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
# 2nd for login page
class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email