from django.db import models
from organizers.models import Category,Tag
from instructors.models import Instructor

class Course(models.Model):
    title = models.CharField(primary_key=True, unique=True, max_length=50)
    # image = models.ImageField(upload_to='course_images/', blank=True, null=True)  # Image upload field
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)  # Max 9.99
    published_status = models.BooleanField(default=False)  # True for published, False for draft
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # One category
    tags = models.ManyToManyField(Tag,on_delete=models.SET_NULL,  null=True, blank=True)  # Multiple tags
    instructor = models.ForeignKey(Instructor, null=True, on_delete=models.SET_NULL)  # One instructor
    # lessons = models.ManyToManyField('Lesson', blank=True, related_name='courses')  # Multiple lessons
    # review = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
