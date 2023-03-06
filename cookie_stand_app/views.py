from rest_framework import generics
from .models import Stand
from .serializer import StandSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class StandList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Stand.objects.all()
    serializer_class = StandSerializer


class StandDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Stand.objects.all()
    serializer_class = StandSerializer

