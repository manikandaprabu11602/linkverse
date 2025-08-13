from django.db import models
from django.contrib.auth.models import User

class LinkCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categories_created')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name


class Link(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to='link_images/')
    category = models.ForeignKey(LinkCategory, on_delete=models.CASCADE, related_name='links')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links_created')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title
