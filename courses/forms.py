from django import forms
from .models import Course
# from organizers.models import Category

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].label = "Course Title"
    #     self.fields['description'].label = "Course Description"
    #     self.fields['price'].label = "Price (up to 9999.99)"
    #     self.fields['published_status'].label = "Published?"
    #     self.fields['category'].queryset = Category.objects.all()
    #     self.fields['cover'].label = "Course Cover"
    #     self.fields['price'].widget = forms.NumberInput(attrs={'step': '0.01'})
    #     self.fields['published_status'].widget = forms.CheckboxInput()
    #     self.fields['cover'].required = False  # Allow updating without changing cover