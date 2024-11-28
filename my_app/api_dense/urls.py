from django.urls import path
from api_dense.views import *

urlpatterns = [
    path('', view_dtl, name='dtl'),
    path('emp/',view_emp, name='emp'),
]