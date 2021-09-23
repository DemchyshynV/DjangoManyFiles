from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser

from .models import CarModel
from .serializers import CarSerializer

class MyView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    parser_classes = (MultiPartParser,)

    def get_serializer_context(self):
        return {'request': self.request}
