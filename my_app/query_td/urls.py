from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('',views.view_td,name='view_td'),
    path('td/', index, name='index'),
    path('member/', views.member, name='member'),
]