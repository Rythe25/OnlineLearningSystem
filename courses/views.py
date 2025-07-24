from django.shortcuts import render, redirect
from users.decorators import role_required

from .models import Course
from .forms import CourseForm
from django.http import HttpResponseNotFound
import os 

@role_required('EMPLOYEE')
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("employee_course")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = CourseForm()
    return render(request, "courses/course_create.html", {
        'form': form,
        'title': 'Create Course'
    })

@role_required('EMPLOYEE')
def course_update(request, pk):
    course = Course.objects.filter(pk=pk).first()
    if not course:
        return redirect("employee_course")
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            course = form.save()
            return redirect("employee_course")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = CourseForm(instance=course)
    return render(request, "courses/course_update.html", {"form": form})

@role_required('EMPLOYEE')
def course_delete(request, pk):
    course = Course.objects.filter(pk=pk).first()
    if not course:
        return HttpResponseNotFound("Course not found")
    if request.method == "POST":
        if course.cover and os.path.isfile(course.cover.path):
            os.remove(course.cover.path)
        course.delete()
        return redirect("employee_course")
    return render(request, "courses/course_delete.html", {"course": course})

@role_required('EMPLOYEE')
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})