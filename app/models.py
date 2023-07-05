from django.db import models
import uuid
from django.utils import timezone

# Create your models here.

class Image(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title