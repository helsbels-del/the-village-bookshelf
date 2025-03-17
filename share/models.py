from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Books(models.Model):
    class Meta:
        verbose_name_plural = "Books"
        unique_together = ('title', 'owner')   # so that user cannot add the same book twice
        ordering = ['title']

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
    genre = models.CharField(max_length=100, blank=True, null=True) 
    
    # User who owns the book
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Is the book available for swap/share
    available = models.BooleanField(default=True)
    
    # Timestamp fields to track when the book is added or modified
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class SwapRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests_made")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name="swap_requests")
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.requester} requested {self.title}"
    