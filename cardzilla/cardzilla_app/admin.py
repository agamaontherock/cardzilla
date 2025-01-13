from django.contrib import admin
from .models import CardSet

@admin.register(CardSet)
class CardSet(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'updated_at']
    raw_id_fields = ['editors', 'viewers']