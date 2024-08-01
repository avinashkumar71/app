from django.db import models
from rest_framework import serializers
# Create your models here.


class CarouselModel(models.Model):
    image_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='carousel/')

    def __str__(self):
        return self.image_name


class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselModel
        fields = '__all__'