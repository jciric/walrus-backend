from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserManager(models.Manager):

    use_in_migrations = True

    def create_user(self, username, email, password=None):

        if not username:
            raise ValueError('The given username must be set')
            email = UserManager.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=False, is_active=True, is_superuser=False,
                         )

        user.set_password(password)

        try:
            user.save(using=self._db)
        except IntegrityError:
            raise ValueError('This email has already been registered.')

        return user

    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lowercasing the domain part of the it.
        """
        email = email or ''
        try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        return email

class users(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    fields = ('username', 'password', 'email')
    objects = UserManager()

    def __str__(self):
            return self.user.username

class Category(models.Model):
    CATEGORIES = (
        ("Music", "music"),
        ("Painting&Drawing", "painting&drawing"),
        ("Photography", "photography"),
    )
    category= models.CharField(max_length=20, choices=CATEGORIES, default=None)

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
