from django.db import models
from organizers.models import Category, Tag
from instructors.models import Instructor
import uuid

def generate_uuid():
    return uuid.uuid4()

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid, editable=False)
    title = models.CharField(unique=True, max_length=50)  # Removed primary_key=True
    cover = models.ImageField(upload_to='course/covers/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=6)  # Max 9999.99
    published_status = models.BooleanField(default=False)  # True for published, False for draft
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # One category
    tags = models.ManyToManyField(Tag, blank=True)  # Multiple tags, removed on_delete
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)  # One instructor
    # lessons = models.ManyToManyField('Lesson', blank=True, related_name='courses')  # Multiple lessons
    # review = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title