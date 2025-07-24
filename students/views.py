from django.shortcuts import render,redirect
from django.contrib import messages
from users.decorators import role_required

from .models import User
from students.models import Student
from lessons.models import Lesson
from instructors.models import Instructor
from courses.models import Course
from organizers.models import Category, Tag
from submissions.models import Submission
from assignments.models import Assignment

@role_required('STUDENT')
def student_home(request):
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    
    instructor_id = request.GET.get('instructor')
    category_id = request.GET.get('category')
    tag_id = request.GET.get('tag')
    
    courses = Course.objects.filter()
    
    if instructor_id:
        courses = courses.filter(instructor__id=instructor_id)
    if category_id:
        courses = courses.filter(category__id=category_id)
    if tag_id:
        courses = courses.filter(tags__id=tag_id)
    
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
        student = Student.objects.get(id=user_id)
        course = Course.objects.get(id=course_id)
        
        if request.method == 'POST' and 'enroll' in request.POST:
            if course not in student.courses.all():
                student.courses.add(course)
                messages.success(request, 'Successfully enrolled in the course.')
                return redirect('student_enrollment', course_id=course.id)
        
        context = {
            'student': student,
            'course': course,
            'is_enrolled': course in student.courses.all(),
        }
        return render(request, 'students/student_enrollment.html', context)
    except (Student.DoesNotExist, Course.DoesNotExist):
        return render(request, 'students/student_enrollment.html', {
            'student': student,
            'error': 'Course or student not found'
        })
        
@role_required('STUDENT')
def student_info(request, course_id=None):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        student = Student.objects.get(id=user_id)
        
        if course_id:
            course = Course.objects.get(id=course_id)
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
    
@role_required('STUDENT')
def student_assignment_list(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        student = Student.objects.get(id=user_id)
        enrolled_courses = Course.objects.filter(students=student, assignment__isnull=False).distinct()
        assignments = Assignment.objects.filter(course__in=enrolled_courses)
        context = {
            'user': user,
            'assignments': assignments,
            'enrolled_courses': enrolled_courses,
        }
        return render(request, 'students/student_assignment_list.html', context)
    except (User.DoesNotExist, Student.DoesNotExist):
        return render(request, 'students/student_assignment_list.html', {'user': user, 'error': 'User or student not found'})

@role_required('STUDENT')
def student_submission(request, assignment_id):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        student = Student.objects.get(id=user_id)
        assignment = Assignment.objects.get(id=assignment_id, course__in=student.courses.all())
        
        if request.method == 'POST':
            file = request.FILES.get('file')
            description = request.POST.get('description')
            if description:
                Submission.objects.create(
                    course=assignment.course,
                    file=file,
                    description=description,
                    student=student 
                )
                messages.success(request, 'Submission uploaded successfully')
                return redirect('student_assignment_list')
        
        context = {
            'user': user,
            'assignment': assignment,
            'course': assignment.course,
        }
        return render(request, 'students/student_submission.html', context)
    except (User.DoesNotExist, Student.DoesNotExist, Assignment.DoesNotExist):
        return render(request, 'students/student_submission.html', {
            'user': user,
            'error': 'User, student, or assignment not found'
        })