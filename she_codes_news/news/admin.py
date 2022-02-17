from django.contrib import admin
from . import models
from .models import NewsStory, Category


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'author', 'slug')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(NewsStory, AuthorAdmin,)
admin.site.register(Category)