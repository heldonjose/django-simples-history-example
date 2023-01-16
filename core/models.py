from django.contrib.auth.models import User
from django.db import models
from simple_history.models import HistoricalRecords

from core.base import BaseModel
from core.choices import CourseStatusChoices


class Category(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Course(BaseModel, CourseStatusChoices):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=CourseStatusChoices.STATUS)
    categories = models.ManyToManyField(Category, blank=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.status != Course.STATUS_ACTIVE:
            self.skip_history_when_saving = False
        super().save(*args, **kwargs)


class Certificate(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    history = HistoricalRecords()
