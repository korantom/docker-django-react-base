from .models import ExampleModel

from rest_framework import viewsets, permissions
from .serializers import ExampleSerializer

# Example Viewset


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = ExampleModel.objects.all()
    permission_classes = [
        permissions.AllowAny,  # temporary
    ]
    serializer_class = ExampleSerializer
