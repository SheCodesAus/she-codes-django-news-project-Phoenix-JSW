from django.contrib import admin
from . import models
from .models import NewsStory


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('status', 'title','slug', 'author')
admin.site.register(NewsStory, AuthorAdmin)