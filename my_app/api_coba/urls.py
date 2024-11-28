from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('messages/create/', views.MessageCreateView.as_view(), name='message-create'),
    path('album/', views.AlbumListView.as_view(), name='album-list'),
    path('album/create/', views.AlbumCreateView.as_view(), name='album-create'),
    path('report/', views.ReportListView.as_view(), name='report-list'),
    path('report/create/', views.ReportCreateView.as_view(), name='report-create'),
]