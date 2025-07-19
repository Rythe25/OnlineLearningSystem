from django.db import models
import uuid

def generate_uuid():
    return uuid.uuid4()

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid(), editable=False)
    title = models.CharField(unique=True, max_length=50)
    
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=generate_uuid(), editable=False)
    title = models.CharField(unique=True, max_length=50)
    
    def __str__(self):
        return self.title