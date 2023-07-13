from django.contrib import admin
from .models import Category, News, User


admin.site.register(Category)
admin.site.register(News)
admin.site.register(User)
