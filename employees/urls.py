from django.urls import path
from . import views
from organizers import views as organizer_views

urlpatterns = [
    path('', views.employee_home, name ='employee_home'),
    path('organizers/', views.employee_organizer, name ='employee_organizer'),
    
    #Category
    path('categories/', organizer_views.category_create, name ='category_create'),
    path('categories/update/<uuid:pk>/', organizer_views.category_update, name ='category_update'),
    path('categories/delete/<uuid:pk>/', organizer_views.category_delete, name ='category_delete'),
    
    #Tag
    path('tags/', organizer_views.tag_create, name ='tag_create'),
    path('tags/update/<uuid:pk>/', organizer_views.tag_update, name ='tag_update'),
    path('tags/delete/<uuid:pk>/', organizer_views.tag_delete, name ='tag_delete'),
]