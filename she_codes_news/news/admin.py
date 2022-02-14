from django.contrib import admin
from . import models
from .models import NewsStory, Category


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'author')
admin.site.register(NewsStory, AuthorAdmin,)
admin.site.register(Category)