from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
