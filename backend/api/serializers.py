from rest_framework import serializers
from api.models import ExampleModel

# ExampleModel Serializer
class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = "__all__"
        # fields = ['name', ...]
