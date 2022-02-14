from asyncio.windows_events import NULL
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
from django.template.defaultfilters import slugify 

class Category(models.Model):
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, default=uuid.uuid4)

    class Meta:
        ordering = ['category']
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.category
    
    def get_absolute_url(self):
        return reverse('#', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class NewsStory(models.Model):

    options = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='stories'
    )
    pub_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='images', null=True, blank=True)
    story_category = models.ManyToManyField(Category, related_name='stories')
    slug = models.SlugField(unique=True, default=uuid.uuid4)
    status = models.CharField(max_length=10, choices=options, default='draft')     
          
    class Meta:
        verbose_name_plural = "news stories"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk': self.pk})
 