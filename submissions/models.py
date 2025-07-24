from django.db import models
from courses.models import Course
from students.models import Student
import uuid

class Submission(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='submissions/files/', null=True, blank=True, help_text="Upload a PDF file for the lesson")
    description = models.TextField()
    student = models.ForeignKey(Student,on_delete=models.SET_NULL, null=True, blank=True)
