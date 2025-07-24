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
    
    # Assignment
    path('assignments/', views.student_assignment_list, name ='student_assignment_list'),
    
    # Submission
    path('submissions/<uuid:assignment_id>/', views.student_submission, name ='student_submission'),
    
]