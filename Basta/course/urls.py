from django.urls import path
from .views import *

urlpatterns = [
    path('', coursehome, name='home'),

]