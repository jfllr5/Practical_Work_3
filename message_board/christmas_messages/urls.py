from django.urls import path
from .views import submit_message, get_messages, delete_message

urlpatterns = [
    path('submit/', submit_message, name='submit_message'),
    path('get/', get_messages, name='get_messages'),
    path('delete/<int:message_id>/', delete_message, name='delete_message'),
]