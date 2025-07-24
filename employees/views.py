from django.shortcuts import render,redirect
from users.decorators import role_required
from django.contrib import messages

from .models import Employee
from students.models import Student
from instructors.models import Instructor
from organizers.models import Category, Tag
from courses.models import Course
from users.models import User

@role_required('EMPLOYEE')
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

@role_required('EMPLOYEE')
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

@role_required('EMPLOYEE')
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
    
@role_required('EMPLOYEE')
def employee_info(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        return render(request, 'employees/employee_info.html', {
            'user': user,
        })
    except Employee.DoesNotExist:
        return render(request, 'employees/employee_info.html', {
            'user': user,
            'error': 'employee profile not found'
        })

@role_required('EMPLOYEE')
def employee_enrollment_list(request):
    user_id = request.session.get('user_id')
    try:
        user = Employee.objects.get(id=user_id)
        courses = Course.objects.all()
        selected_course_id = request.GET.get('course_id')
        
        if selected_course_id:
            students = Student.objects.filter(courses__id=selected_course_id)
        else:
            students = Student.objects.filter(courses__isnull=False).distinct()
            
        context = {
            'user': user,
            'students': students,
            'courses': courses,
            'selected_course_id': selected_course_id,
        }
        return render(request, 'employees/employee_enrollment_list.html', context)
    except Employee.DoesNotExist:
        return redirect('login')

@role_required('EMPLOYEE')
def employee_enrollment(request, student_id):
    user_id = request.session.get('user_id')
    try:
        user = Employee.objects.get(id=user_id)
        student = Student.objects.get(id=student_id)
        
        if request.method == 'POST' and 'unenroll' in request.POST:
            course_id = request.POST.get('course_id')
            course = Course.objects.get(id=course_id)
            student.courses.remove(course)
            messages.success(request, f'Successfully unenrolled {student.name} from {course.title}.')
            return redirect('employee_enrollment', student_id=student.id)
        
        context = {
            'user': user,
            'student': student,
            'enrolled_courses': student.courses.all(),
        }
        return render(request, 'employees/employee_enrollment.html', context)
    except (Employee.DoesNotExist, Student.DoesNotExist, Course.DoesNotExist):
        return render(request, 'employees/employee_enrollment.html', {
            'user': user,
            'error': 'Employee, student, or course not found'
        })
        
@role_required('EMPLOYEE')
def employee_student_detail(request, student_id):
    user_id = request.session.get('user_id')
    try:
        user = Employee.objects.get(id=user_id)
        student = Student.objects.get(id=student_id)

        context = {
            'user': user,
            'student': student,
        }
        return render(request, 'employees/employee_student_detail.html', context)
    except (Employee.DoesNotExist, Student.DoesNotExist):
        return render(request, 'employees/employee_student_detail.html', {
            'user': user,
            'error': 'Employee, Student not found'
        })
        
@role_required('EMPLOYEE')
def employee_instructor_detail(request, instructor_id):
    user_id = request.session.get('user_id')
    try:
        user = Employee.objects.get(id=user_id)
        instructor = Instructor.objects.get(id=instructor_id)

        context = {
            'user': user,
            'instructor': instructor,
        }
        return render(request, 'employees/employee_instructor_detail.html', context)
    except (Employee.DoesNotExist, Instructor.DoesNotExist):
        return render(request, 'employees/employee_instructor_detail.html', {
            'user': user,
            'error': 'Employee or instructor not found'
        })