from django.urls import path
from .views import *

urlpatterns = [
    path('learn/', learn, name='learn'),
    path('catalog/', catalog, name='catalog'),
    path('course/', course, name='course')
]
