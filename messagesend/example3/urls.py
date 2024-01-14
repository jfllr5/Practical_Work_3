from django.urls import path
from .views import submit_message, get_message
from . import views

urlpatterns = [
    path('submit/', submit_message, name='submit_message'),
    path('get/<str:recipient_name>/', get_message, name='get_message'),
    
]  
