from django.db import models


# Create your models here.
class CarModel(models.Model):
    class Meta:
        db_table = 'car'

    brand = models.CharField(max_length=20)


class ImagesModel(models.Model):
    class Meta:
        db_table = 'photos'
    photo = models.ImageField(upload_to='photo')
    car = models.ForeignKey(CarModel, related_name='images', on_delete=models.CASCADE)
