from rest_framework import serializers, viewsets

from .models import Container


class ContainerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Container
        fields = '__all__'

class ContainerViewSet(viewsets.ModelViewSet):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer