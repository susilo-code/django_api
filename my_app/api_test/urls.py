# app - urls.py file

from django.urls import path
from api_test.views import *

urlpatterns = [
    path('', view_dtl, name='dtl'),
    path('person/',view_person, name='person'),
    path('member/',view_member, name='member'),
]