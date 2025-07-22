from django.shortcuts import render
from django.contrib import messages
from .models import User
from students.models import Student
from lessons.models import Lesson
from instructors.models import Instructor
from courses.models import Course
from organizers.models import Category, Tag
from users.decorators import role_required

@role_required('STUDENT')
def student_home(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    
    # Get filter parameters
    instructor_id = request.GET.get('instructor')
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')
    
    # Start with all published courses
    courses = Course.objects.filter(published_status=True)
    
    # Apply filters
    if instructor_id:
        courses = courses.filter(instructor__id=instructor_id)
    if category_id:
        courses = courses.filter(category__id=category_id)
    if tag_id:
        courses = courses.filter(tags__id=tag_id)
    
    # Get filter options
    instructors = Instructor.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'user': user,
        'courses': courses,
        'instructors': instructors,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'students/student_home.html', context)

@role_required('STUDENT')
def student_enrollment(request, course_id):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        course = Course.objects.get(id=course_id, published_status=True)
        context = {
            'user': user,
            'course': course,
        }
        return render(request, 'students/student_enrollment.html', context)
    except (User.DoesNotExist, Course.DoesNotExist):
        return render(request, 'students/student_enrollment.html', {'user': user, 'error': 'Course or user not found'})

@role_required('STUDENT')
def student_info(request, course_id=None):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        student = Student.objects.get(id=user_id)
        
        # Handle course enrollment
        if course_id:
            course = Course.objects.get(id=course_id, published_status=True)
            student.courses.add(course)
            messages.success(request, f'Enrolled in {course.title}')
        
        context = {
            'user': user,
            'student': student,
            'enrolled_courses': student.courses.all(),
        }
        return render(request, 'students/student_info.html', context)
    except (User.DoesNotExist, Student.DoesNotExist, Course.DoesNotExist):
        return render(request, 'students/student_info.html', {'user': user, 'error': 'User, student, or course not found'})
    
@role_required('STUDENT')
def student_lesson_list(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        student = Student.objects.get(id=user_id)
        enrolled_courses = student.courses.all()
        lessons = Lesson.objects.filter(course__in=enrolled_courses)
        context = {
            'user': user,
            'lessons': lessons,
            'enrolled_courses': enrolled_courses,
        }
        return render(request, 'students/student_lesson_list.html', context)
    except (User.DoesNotExist, Student.DoesNotExist):
        return render(request, 'students/student_lesson_list.html', {'user': user, 'error': 'User or student not found'})

@role_required('STUDENT')
def student_lesson(request, lesson_id):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        student = Student.objects.get(id=user_id)
        lesson = Lesson.objects.get(id=lesson_id, course__in=student.courses.all())
        context = {
            'user': user,
            'lesson': lesson,
            'course': lesson.course,
        }
        return render(request, 'students/student_lesson.html', context)
    except (User.DoesNotExist, Student.DoesNotExist, Lesson.DoesNotExist):
        return render(request, 'students/student_lesson.html', {'user': user, 'error': 'User, student, or lesson not found'})