from rest_framework import serializers
from shop.models import Factory


class FactorySerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Factory
        fields = ('name', 'user', 'product',)
