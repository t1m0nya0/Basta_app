from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить курс", 'url_name': 'add_course'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}, ]


def learn(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
        'menu': menu,
        'title': 'My learn',
        'cat_selected': 0,
    }

    return render(request, 'course/index.html', context=context)


def catalog(request):
    pass


def about(request):
    return render(request, 'course/about.html', {'menu': menu, 'title': 'О сайте'})


def addcourse(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('learn')
    else:
        form = AddCourseForm()
    return render(request, 'course/addcourse.html', {'form': form, 'menu': menu, 'title': 'Добавление курса'})


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
        'menu': menu,
        'title': course.title,
        'cat_selected': course.category_id,
    }

    return render(request, 'course/post.html', context=context)


def show_category(request, category_id):
    courses = Course.objects.filter(category_id=category_id)

    if len(courses) == 0:
        raise Http404()

    context = {
        'courses': courses,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': category_id,
    }

    return render(request, 'course/index.html', context=context)
