from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s' % (self.name)
