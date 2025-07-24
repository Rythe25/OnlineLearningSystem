from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'course', 'description', 'video', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter lesson title'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter lesson description'}),
            'video': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enter video URL (e.g., YouTube or Vimeo link)'}),
            'file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf'}),
        }
        labels = {
            'title': 'Lesson Title',
            'course': 'Course',
            'description': 'Description',
            'video': 'Video URL',
            'file': 'Lesson File (PDF)',
        }