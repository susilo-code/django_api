from rest_framework import serializers
from api_test.models import Person
from query_td.models import Member

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields='__all__'