from django.contrib import admin
from users.models import users, Content, Category

# Register your models here.
admin.site.register(users)
admin.site.register(Content)
admin.site.register(Category)
