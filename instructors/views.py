from django.shortcuts import render
from lessons.models import Lesson

def lesson_view(request):
    lessons = Lesson.objects.all()
    return render(request,"lessons/lesson_view.html",{"lessons":lessons})
