from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


"""class CourseHome(ListView):
    template_name = 'course/index.html'"""


def learn(request):
    return render(request, 'course/index.html')


def catalog(request):
    pass


def course(request):
    pass
