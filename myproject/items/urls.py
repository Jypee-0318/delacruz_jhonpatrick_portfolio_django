from django.urls import path
from .views import AddItems, GetItems, GettheItems, UpdateItems, DeleteItems

app_name = "items"

urlpatterns = [
    path('', GetItems, name='GetItems'),
    path('<int:item_id>', GettheItems, name='GettheItems'),
    path('add/', AddItems, name='AddItems'),
    path('update/<int:item_id>', UpdateItems, name='UpdateItems'),
    path('delete/<int:item_id>', DeleteItems, name='DeleteItems'),
]