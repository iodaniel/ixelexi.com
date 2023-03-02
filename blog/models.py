from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



STATUS = ((0, "Draft"),(1, "Publish"))

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    content = models.TextField()
    cover = models.ImageField(upload_to='images/', null=False, blank=False)
    status = models.IntegerField(choices = STATUS, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['create_at']


    def __str__(self):
        return self.title