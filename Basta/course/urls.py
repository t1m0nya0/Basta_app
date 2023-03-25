from django.urls import path
from .views import *

urlpatterns = [
    path('', course_home, name='home'),
]
