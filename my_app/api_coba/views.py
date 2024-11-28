from django.shortcuts import render
from rest_framework.response import Response
from .models import Message,Album, Report
from .serializers import MessageSerializer,AlbumSerializer,ReportSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
import requests

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get']

class AlbumCreateView(generics.CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artist']
    http_method_names = ['get']

class ReportCreateView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author','topic']
    http_method_names = ['get']

# class ReportDeleteView(generics.DestroyAPIView):
#     data=ReportSerializer.data
#     queryset = Report.objects.get()
#     serializer_class = ReportSerializer
#     filter_backends = [DjangoFilterBackend]
#     permission_classes = [permissions.IsAuthenticated]
#     filterset_fields = ['author','topic']
#     http_method_names = ['delete']
    