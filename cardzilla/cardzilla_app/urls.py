from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    # path('/cardset/create', cardset_create, name='cardset_create'),
    # path('/cardset/delete', cardset_delete, name='cardset_delete'),
    # path('/cardset/update', cardset_update, name='cardset_update'),
    path('cardset/view', CardSetListView.as_view(), name='cardset_view'),
]
