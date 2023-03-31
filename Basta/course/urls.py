from django.urls import path
from .views import *

urlpatterns = [
    path('learn/', Learn.as_view(), name='learn'),
    path('catalog/', catalog, name='catalog'),
    path('about/', about, name='about'),
    path('addcourse/', addcourse, name='add_course'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('course/<int:course_id>/', show_course, name='course'),
    path('category/<int:category_id>/', show_category, name='category'),

]
