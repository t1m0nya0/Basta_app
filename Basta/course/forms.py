from django import forms
from .models import *


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
