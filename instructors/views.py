from django.shortcuts import render, redirect
from courses.models import Course
from lessons.models import Lesson
from assignments.models import Assignment
from instructors.models import Instructor
from users.decorators import login_required, role_required
from users.models import User

@role_required('INSTRUCTOR')
def instructor_home(request):
    if (request.user.role is not 'INSTRUCTOR'):
        return redirect('login')
    return render(request, 'instructors/instructor_home.html')

@role_required('INSTRUCTOR')
def instructor_course(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        instructor = Instructor.objects.get(id=user_id)
        courses = Course.objects.filter(instructor=instructor)
        return render(request, 'instructors/instructor_course.html', {'courses': courses, 'user': user})
    except Instructor.DoesNotExist:
        return render(request, 'instructors/instructor_course.html', {'courses': [], 'user': user, 'error': 'Instructor profile not found'})

@role_required('INSTRUCTOR')
def instructor_lesson(request):
    lessons = Lesson.objects.all()
    return render(request,"instructors/instructor_lesson.html",{"lessons":lessons})

@role_required('INSTRUCTOR')
def instructor_assignment(request):
    assignments = Assignment.objects.all()
    return render(request,"instructors/instructor_assignment.html",{"assignments":assignments})
