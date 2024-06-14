from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import datetime

class Review(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=datetime.now())
    
    
    def __str__(self):
        return f'{self.user_name} rated us {self.rating} stars'
