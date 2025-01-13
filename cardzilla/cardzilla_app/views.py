from django.shortcuts import render
from django.views.generic import ListView
from .models import CardSet

# Create your views here.
class CardSetListView(ListView):
    model = CardSet
    # paginate_by = 5
    queryset = CardSet.objects.all()