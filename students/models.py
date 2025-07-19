from django.db import models
from users.models import User

class Student(User):
    pass

    def __str__(self):
        return f"{self.name} (Student)"