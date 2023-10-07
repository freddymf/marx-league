from django.db import models
import os


def image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = 'uno.{}'.format(ext)
    return os.path.join('news/', new_filename)

class News(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to=image_upload_path, null=True, blank=True)
    caption = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
    
    
