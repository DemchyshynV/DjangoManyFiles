from rest_framework import serializers as s
from rest_framework.request import Request

from .models import ImagesModel, CarModel


class ImageSerializer(s.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = ('photo',)


class CarSerializer(s.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('brand',)

    def create(self, validated_data):
        request: Request = self.context.get('request')
        car = CarModel.objects.create(**validated_data)
        for image in request.FILES:
            serializer = ImageSerializer(data={'photo': request.FILES[image]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        return car
