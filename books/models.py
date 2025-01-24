from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    img = models.URLField(max_length=500)
    summary = models.TextField()

    def __str__(self):
        return self.name
