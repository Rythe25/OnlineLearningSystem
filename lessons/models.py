from django.db import models
from courses.models import Course
import uuid

class Lesson(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(unique=True, max_length=50)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    video = models.URLField(max_length=200, null=True, blank=True, help_text="Embed URL (YouTube)")
    pdf = models.FileField(upload_to='lessons/files/', null=True, blank=True, help_text="Upload a PDF file for the lesson")
    
    def __str__(self):
        return self.title
