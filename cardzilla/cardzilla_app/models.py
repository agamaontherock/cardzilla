from django.db import models
from django.conf import settings

class CardSet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    editors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cardsets_editable')
    viewers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cardsets_viewable')
    
    def __str__(self):
        return self.name
