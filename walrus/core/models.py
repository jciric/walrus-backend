from django.db import models
from users.models import users

# Create your models here.
class Category(models.Model):
    CATEGORIES = (
        ("Music", "music"),
        ("Painting&Drawing", "painting&drawing"),
        ("Photography", "photography"),
    )
    category = models.CharField(max_length=20, choices=CATEGORIES, default=None)

    def __str__(self):
        return self.category

class Content(models.Model):
    title = models.CharField(max_length=100)
    owner = models.OneToOneField(users, on_delete=models.CASCADE, default="")
    tag =  models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        default= "",
    )
    fields = ('username')
    description = models.TextField()
    date_created = models.DateField(auto_now=True,)

    class Meta:
        ordering = ('title',)

        def __str__(self):
            return '{} - {}'.format(self.title, self.username)

# Create your models here.
