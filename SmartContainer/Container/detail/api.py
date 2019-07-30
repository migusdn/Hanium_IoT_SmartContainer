from rest_framework import serializers, viewsets

from .models import Detail


class DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detail
        fields = '__all__'

class DetailViewSet(viewsets.ModelViewSet):
    queryset = Detail.objects.all()
    serializer_class = DetailSerializer