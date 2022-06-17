from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Post(models.Model):
    Title =  models.TextField(max_length=200)
    Text = models.TimeField() 
    Author =  models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

    def __str__(self):
        return self.Title

    