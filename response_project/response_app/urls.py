from django.urls import path
from .views import HttpResponseExample

urlpatterns = [
    path('example/', HttpResponseExample.as_view(), name='response_example'),
]