from django.shortcuts import render
from students.models import Student
from instructors.models import Instructor
from organizers.models import Category, Tag

def employee_home(request):
    students = Student.objects.all()
    instructors = Instructor.objects.all()
    return render(request, 'employees/employee_home.html',{
        'students' : students,
        'instructors' : instructors
    })
    
def employee_organizer(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'employees/employee_organizer.html',{
        'categories' : categories,
        'tags' : tags
    })