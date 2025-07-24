from django.shortcuts import render, redirect
from users.decorators import role_required
import os

from users.models import User
from courses.models import Course
from lessons.models import Lesson
from assignments.models import Assignment
from instructors.models import Instructor
from submissions.models import Submission

@role_required('INSTRUCTOR')
def instructor_home(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        instructor = Instructor.objects.get(id=user_id)
        courses = Course.objects.filter(instructor=instructor)
        return render(request, 'instructors/instructor_home.html', {'courses': courses, 'user': user})
    except Instructor.DoesNotExist:
        return render(request, 'instructors/instructor_home.html', {'courses': [], 'user': user, 'error': 'Instructor profile not found'})

@role_required('INSTRUCTOR')
def instructor_lesson(request):
    lessons = Lesson.objects.all()
    return render(request,"instructors/instructor_lesson.html",{"lessons":lessons})

@role_required('INSTRUCTOR')
def instructor_assignment(request):
    assignments = Assignment.objects.all()
    return render(request,"instructors/instructor_assignment.html",{"assignments":assignments})

@role_required('INSTRUCTOR')
def instructor_info(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        instructor = Instructor.objects.get(id=user_id)
        courses = Course.objects.filter(instructor=instructor)
        return render(request, 'instructors/instructor_info.html', {
            'user': user,
            'courses': courses
        })
    except Instructor.DoesNotExist:
        return render(request, 'instructors/instructor_info.html', {
            'user': user,
            'error': 'Instructor profile not found'
        })

@role_required('INSTRUCTOR')
def instructor_submission_list(request):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        instructor = Instructor.objects.get(id=user_id)
        courses = Course.objects.filter(instructor=instructor)
        course_id = request.GET.get('course_id')
        submissions = Submission.objects.filter(course__in=courses)
        if course_id:
            submissions = submissions.filter(course__id=course_id)
        return render(request, 'instructors/instructor_submission_list.html', {
            'courses': courses,
            'submissions': submissions,
            'user': user,
            'selected_course': course_id
        })
    except Instructor.DoesNotExist:
        return render(request, 'instructors/instructor_submission_list.html', {
            'courses': [],
            'submissions': [],
            'user': user,
            'error': 'Instructor profile not found'
        })

@role_required('INSTRUCTOR')
def instructor_submission(request, submission_id):
    user_id = request.session.get('user_id')
    try:
        user = User.objects.get(id=user_id)
        submission = Submission.objects.get(id=submission_id)
        return render(request, 'instructors/instructor_submission.html', {
            'submission': submission,
            'course': submission.course,
            'user': user
        })
    except (Submission.DoesNotExist, Instructor.DoesNotExist):
        return render(request, 'instructors/instructor_submission.html', {
            'user': user,
            'error': 'Submission or instructor profile not found'
        })


@role_required('INSTRUCTOR')
def instructor_submission_reject(request, submission_id):
    submission = Submission.objects.filter(pk=submission_id).first()
    if not submission:
        return redirect('instructor_submission_list')
    if request.method == 'POST':
        if submission.file and os.path.isfile(submission.file.path):
            os.remove(submission.file.path)
        submission.delete()
        return redirect('instructor_submission_list')
    return render(request, 'instructors/instructor_submission_reject.html', {'submission': submission})
        
        
