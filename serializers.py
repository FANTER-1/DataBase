from rest_framework import serializers
from .models import SubmitData

class SubmitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitData
        fields = '__all__'