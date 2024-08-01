from django.db import models
from autoslug import AutoSlugField
from category.models import CategoryModel

# Create your models here.


class ProductsModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_slug = AutoSlugField(populate_from='product_name')
    product_image = models.ImageField(upload_to='productsImages/')
    category = models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    price = models.FloatField()
    stock_quantity = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name