from django.urls import path
from .views import index, runcode

urlpatterns = [
    path('', index, name='index'),
    path('runcode/', runcode, name='runcode'),
]