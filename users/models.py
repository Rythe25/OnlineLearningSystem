import uuid
from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True)
    password = models.CharField(max_length=128)  # Will be hashed manually or via form
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=20, choices=[('EMPLOYEE', 'Employee'),
                                                    ('INSTRUCTOR', 'Instructor'),
                                                    ('STUDENT', 'Student')],
                            default='EMPLOYEE')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)