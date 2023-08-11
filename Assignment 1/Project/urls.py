from django.urls import path
from .views import Index, Detail

urlpatterns = [
    path("index", Index, name='Index'),
    path("detail", Detail, name='Detail'),
]
