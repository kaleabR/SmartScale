from django.urls import path
from .views import scale

urlpatterns = [
    path('', scale, name='scale'),
]
