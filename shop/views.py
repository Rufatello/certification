
from rest_framework import generics
from rest_framework.permissions import AllowAny

from shop.serializers import FactorySerializers


class FactoryCreateApiView(generics.CreateAPIView):
    serializer_class = FactorySerializers
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        new_factory = serializer.save(user=self.request.user)
