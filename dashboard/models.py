from django.db import models
from colorfield.fields import ColorField

class SiteSetting(models.Model):
    name = models.CharField(max_length=100)
    color = ColorField(default="000000")

    def __str__(self):
        return self.name
