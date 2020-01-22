from .models import Maserati
from .serializers import MaseratiSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

class MaseratiList(generics.ListCreateAPIView):
    queryset = Maserati.objects.all()
    serializer_class = MaseratiSerializer


class MaseratiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Maserati.objects.all()
    serializer_class = MaseratiSerializer
    permission_classes = (
        IsAuthorOrReadOnly,
    )