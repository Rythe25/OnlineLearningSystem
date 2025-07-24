from django.urls import path
from . import views
from organizers import views as organizer_views
from courses import views as course_views

urlpatterns = [
    path('', views.employee_home, name ='employee_home'),
    path('organizers/', views.employee_organizer, name ='employee_organizer'),
    
    # Student
    path('students/detail/<uuid:student_id>', views.employee_student_detail, name ='employee_student_detail'),
    
    # Instructor
    path('instructors/detail/<uuid:instructor_id>', views.employee_instructor_detail, name ='employee_instructor_detail'),
    
    # Category
    path('categories/create/', organizer_views.category_create, name ='category_create'),
    path('categories/update/<uuid:pk>/', organizer_views.category_update, name ='category_update'),
    path('categories/delete/<uuid:pk>/', organizer_views.category_delete, name ='category_delete'),
    
    # Tag
    path('tags/create/', organizer_views.tag_create, name ='tag_create'),
    path('tags/update/<uuid:pk>/', organizer_views.tag_update, name ='tag_update'),
    path('tags/delete/<uuid:pk>/', organizer_views.tag_delete, name ='tag_delete'),
    
    # Course
    path('courses/', views.employee_course, name='employee_course'),
    path('courses/create/', course_views.course_create , name ='course_create'),
    path('courses/detail/<uuid:pk>/', course_views.course_detail , name ='course_detail'),
    path('courses/update/<uuid:pk>/', course_views.course_update , name ='course_update'),
    path('courses/delete/<uuid:pk>/', course_views.course_delete , name ='course_delete'),
    
    # Enrollment
    path('enrollments/', views.employee_enrollment_list, name='employee_enrollment_list'),
    path('enrollments/<uuid:student_id>/', views.employee_enrollment, name='employee_enrollment'),
    
    # Info
    path('infos/', views.employee_info, name ='employee_info'),
]