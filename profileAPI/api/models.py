from django.db import models
from django.core import validators
# Create your models here.

# create Profile model
class Profile(models.Model):
    profile_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(validators=[validators.EmailValidator(message='Invalid Email')])
    bio=models.TextField()
    profile_picture=models.ImageField(upload_to='images/', default='Images/None/Noimg.jpg')

