from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    title = models.CharField(null=False, blank=False, max_length=100)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(null=False, blank=False, max_length=500)

    def __str__(self):
        return self.description
