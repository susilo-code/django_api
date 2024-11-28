from rest_framework import serializers
from .models import Message,Album,Report

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content']
        # '__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__' 
        # '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__' 