from django.db import models
from users.models import User
from courses.models import Course

class Student(User):
    courses = models.ManyToManyField(Course, blank=True, related_name='students')
    pass

    def __str__(self):
        return f"{self.name} (Student)"