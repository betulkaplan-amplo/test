from dataclasses import fields
from .models import TestModel
from rest_framework import serializers

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'