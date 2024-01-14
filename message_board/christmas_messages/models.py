
from django.db import models

class ChristmasMessage(models.Model):
    sender_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='')  # Ajout de default=''
    city = models.CharField(max_length=100, default='')  # Ajout de default=''
    gift_list = models.TextField()
    kindness_level = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    has_cavities = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)
    class Meta:
        app_label = 'christmas_messages'