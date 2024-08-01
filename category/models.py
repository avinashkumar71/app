from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = AutoSlugField(populate_from='category_name')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name