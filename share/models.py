from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Books(models.Model):
    # Basic details about the book
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  

# Book condition: you can use a choice field to limit the options
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('LIKE_NEW', 'Like New'),
        ('POOR', 'Poor'),
    ]
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default='USED')
    
    # Book category or genre (optional)
    genre = models.CharField(max_length=100, blank=True, null=True)  # Could be a ForeignKey if you want more structure
    
    # User who owns the book (if you plan to associate users with books)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Timestamp fields to track when the book is added or modified
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

    