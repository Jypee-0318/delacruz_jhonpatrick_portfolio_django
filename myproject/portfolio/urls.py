from django.urls import path
from .views import index
from .views import dashboard
from .views import portfolio

app_name = "portfolio"

urlpatterns = [
    path('', index, name='index'),
    path('portfolio/', portfolio, name='portfolio'),
    path('dashboard/', dashboard, name='dashboard'),
]