from rest_framework.generics import ListCreateAPIView

from .models import CarModel
from .serializers import CarSerializer


class MyView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_serializer_context(self):
        return {'request': self.request}
