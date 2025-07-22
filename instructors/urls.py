from django.urls import path
from . import views
from lessons import views as lesson_views
from assignments import views as assignment_views

urlpatterns = [
    path('', views.instructor_home, name='instructor_home'),
    
    #Course
    path('courses/', views.instructor_course, name='instructor_course'),
    
    # Lesson
    path('lessons/', views.instructor_lesson, name ='instructor_lesson'),
    path('lessons/create/', lesson_views.lesson_create, name ='lesson_create'),
    path('lessons/update/<uuid:pk>/', lesson_views.lesson_update, name ='lesson_update'),
    path('lessons/delete/<uuid:pk>/', lesson_views.lesson_delete, name ='lesson_delete'),
    
    # Assignment
    path('assignments/', views.instructor_assignment, name ='instructor_assignment'),
    path('assignments/create/', assignment_views.assignment_create, name ='assignment_create'),
    path('assignments/update/<uuid:pk>/', assignment_views.assignment_update, name ='assignment_update'),
    path('assignments/delete/<uuid:pk>/', assignment_views.assignment_delete, name ='assignment_delete'),
    
]