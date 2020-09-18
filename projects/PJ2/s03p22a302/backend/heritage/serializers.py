from rest_framework import serializers
from .models import Heritage


# 문화재 리스트 

class HeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = ('__all__')


class HeritageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heritage
        fields = ('__all__')


