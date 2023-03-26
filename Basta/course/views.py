from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.


"""class CourseHome(ListView):
    template_name = 'course/index.html'"""


def course_home(request):
    return render(request, 'course/index.html')
