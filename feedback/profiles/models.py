from django.db import models

# Create your models here.

class UserProfile(models.Model):
    # user_image = models.FileField(upload_to="images")
    user_image = models.ImageField(upload_to="images")