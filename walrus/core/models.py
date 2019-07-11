from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Content(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    CATEGORIES = (
        ("music", "Music"),
        ("painting&drawing", "Painting&Drawing"),
        ("photography", "Photography"),
    )

    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=None)
    category = models.CharField(max_length=20, choices=CATEGORIES, default=None)
    date_published = models.DateTimeField(auto_now=True)
    fields = ('username')
    description = models.TextField()
    date_created = models.DateField(auto_now=True,)

    class Meta:
        ordering = ('date_published',)

        def __str__(self):
            return '{} - {}'.format(self.title, self.username)
    @classmethod
    def create(cls, title, owner, status, category, date_published):
        post = cls(title=title, owner=owner, status=status, category=category, descriptions=None)
        post.save()

# Create your models here.
