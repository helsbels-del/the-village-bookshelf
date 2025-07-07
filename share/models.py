from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    class Meta:
        verbose_name_plural = "Books"
        unique_together = (
            'title', 'owner')  # Prevent duplicate titles per user
        ordering = ['title']

    # Basic details about the book
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    # Book condition choices
    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('USED', 'Used'),
        ('LIKE_NEW', 'Like New'),
        ('POOR', 'Poor'),
    ]
    condition = models.CharField(
        max_length=10,
        choices=CONDITION_CHOICES,
        default='USED'
    )

    # Optional genre/category
    genre = models.CharField(max_length=100, blank=True, null=True)

    # Linked user who owns the book
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # Availability toggle
    available = models.BooleanField(default=True)

    # Timestamps
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"


class SwapRequest(models.Model):
    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="requests_made"
    )
    book = models.ForeignKey(
        Books,
        on_delete=models.CASCADE,
        related_name="swap_requests"
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester} requested {self.book.title}"
