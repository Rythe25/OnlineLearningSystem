from django.shortcuts import render,redirect
from students.models import Student
from instructors.models import Instructor
from organizers.models import Category, Tag
from courses.models import Course
from users.models import User
from users.decorators import role_required

role_required('EMPLOYEE')
def employee_home(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        students = Student.objects.all()
        instructors = Instructor.objects.all()
        return render(request, 'employees/employee_home.html', {
            'user': user,
            'students': students,
            'instructors': instructors
        })
    except User.DoesNotExist:
        return redirect('login')

role_required('EMPLOYEE')
def employee_organizer(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        categories = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, 'employees/employee_organizer.html', {
            'user': user,
            'categories': categories,
            'tags': tags
        })
    except User.DoesNotExist:
        return redirect('login')

role_required('EMPLOYEE')
def employee_course(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        courses = Course.objects.all()
        return render(request, 'employees/employee_course.html', {
            'user': user,
            'courses': courses
        })
    except User.DoesNotExist:
        return redirect('login')