from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
from django.template.defaultfilters import slugify 

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "categories"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('news:category', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

STATUS = (
    (0,'Draft'),
    (1,'Published')
    )        

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
    image = models.URLField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='stories')
    slug = models.SlugField(unique=True, default=uuid.uuid4)
    status = models.CharField(max_length=10, choices=options, default='draft')     
          
    class Meta:
        verbose_name_plural = "news stories"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk': self.pk})

class Comment(models.Model):
    story = models.ForeignKey(NewsStory, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f"Comment [{self.content}] by {self.name}."

    def approve(self):
        self.approved = True
        self.save()
 