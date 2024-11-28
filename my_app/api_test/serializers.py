from rest_framework import serializers
from api_test.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'