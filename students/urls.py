from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_home, name='student_home'),
    
    #Enrollment
    path('enrollments/<uuid:course_id>/', views.student_enrollment, name='student_enrollment'),
    
    #Info
    path('infos/', views.student_info, name='student_info'),
    path('infos/<uuid:course_id>/', views.student_info, name='student_info'),
    
    # # Lesson
    path('lessons/', views.student_lesson_list, name='student_lesson_list'),
        path('lessons/<uuid:lesson_id>/', views.student_lesson, name='student_lesson'),
    # path('lessons/create/', lesson_views.lesson_create, name ='lesson_create'),
    # path('lessons/update/<uuid:pk>/', lesson_views.lesson_update, name ='lesson_update'),
    # path('lessons/delete/<uuid:pk>/', lesson_views.lesson_delete, name ='lesson_delete'),
    
    # # Assignment
    # path('assignments/', views.instructor_assignment, name ='instructor_assignment'),
    # path('assignments/create/', assignment_views.assignment_create, name ='assignment_create'),
    # path('assignments/update/<uuid:pk>/', assignment_views.assignment_update, name ='assignment_update'),
    # path('assignments/delete/<uuid:pk>/', assignment_views.assignment_delete, name ='assignment_delete'),
    
]