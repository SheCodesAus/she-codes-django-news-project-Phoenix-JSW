from django.contrib import admin
from . import models
from .models import NewsStory, Category, Comment


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('status', 'title', 'author', 'slug')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'story', 'pub_date', 'approved')
    list_filter = ('approved', 'pub_date')
    search_fields = ('name', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

admin.site.register(NewsStory, AuthorAdmin,)
admin.site.register(Category)