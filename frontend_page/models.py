from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('blog_details', args=(str(self.id)))
        return reverse('blog')


class Imageblog(models.Model):
    picture = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=300, null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorized')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog'

    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('blog_details', args=(str(self.id)))
        return reverse('blog')

