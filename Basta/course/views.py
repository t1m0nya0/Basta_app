from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.


"""class CourseHome(ListView):
    template_name = 'course/index.html'"""
menu = ['Catalog', 'Learning']

def learn(request):
    context = {
        'menu': menu,
        'courses': Course.objects.all(),
        'title': 'My learn'
    }
    return render(request, 'course/index.html', context=context)


def catalog(request):
    pass


def course(request):
    pass
