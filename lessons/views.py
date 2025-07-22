from django.shortcuts import render, redirect
from .models import Lesson
from .forms import LessonForm
from django.http import HttpResponseNotFound
import os

def lesson_create(request):
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("instructor_lesson")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = LessonForm()
    return render(request,"lessons/lesson_create.html",{
        "form":form,
        'title': 'Create Lesson'
    })

def lesson_update(request,pk):
    lesson = Lesson.objects.filter(pk = pk).first()
    if not lesson:
        return redirect("instructor_lesson")
    
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES,instance = lesson)
        if form.is_valid():
            form.save()
            return redirect("instructor_lesson")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = LessonForm(instance=lesson)
    return render(request,"lessons/lesson_update.html",{"form":form})

def lesson_delete(request,pk):
    lesson = Lesson.objects.filter(pk = pk).first()
    if not lesson:
        return HttpResponseNotFound("Lesson not found")
    
    if request.method == "POST":
        if lesson.file and os.path.isfile(lesson.file.path):
            os.remove(lesson.file.path)
        lesson.delete()
        return redirect("instructor_lesson")
    return render(request, "lessons/lesson_delete.html", {"lesson": lesson})
