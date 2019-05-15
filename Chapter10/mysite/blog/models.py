from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published'),
    }

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish_date')
    author = models.ForeignKey(User, related_name='blog_posts',
                               on_delete=models.DO_NOTHING)
    body = models.TextField()

    publish_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish_date.year,
            self.publish_date.strftime('%m'),
            self.publish_date.strftime('%d'),
            self.slug
        ])
