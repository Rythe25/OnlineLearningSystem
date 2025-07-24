from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'cover', 'description', 'price', 'category', 'tags', 'instructor']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter course title'}),
            'cover': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter course description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Enter price'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'instructor': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }
        labels = {
            'title': 'Course Title',
            'cover': 'Course Cover Image',
            'description': 'Description',
            'price': 'Price ($)',
            'category': 'Category',
            'tags': 'Tags',
            'instructor': 'Instructors',
        }