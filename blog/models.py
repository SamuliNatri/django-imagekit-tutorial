from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import Thumbnail


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, default='')
    body = models.TextField(blank=False, default='')
    slug = models.SlugField(max_length=255, blank=False, unique=True)
    image = models.ImageField(upload_to='images', default='')
    image_thumbnail = ImageSpecField(source='image',
                                  processors=[Thumbnail(200, 100)],
                                  format='JPEG',
                                  options={'quality': 60})

    def __str__(self):
        return self.title
