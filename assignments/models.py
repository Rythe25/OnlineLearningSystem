from django.db import models
from courses.models import Course
import uuid

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(unique=True, max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to='assignments/files/', null=True, blank=True, help_text="Upload a PDF file for the lesson")
    
    def __str__(self):
        return self.title
