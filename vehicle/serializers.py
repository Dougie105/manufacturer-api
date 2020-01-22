from rest_framework import serializers
from .models import Maserati

class MaseratiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maserati
        fields = [
            'year', 'model', 'description', 'recieved', 'updated'
        ]
