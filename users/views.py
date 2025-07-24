from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login
from django.contrib import messages
from .models import User
from employees.models import Employee
from instructors.models import Instructor
from students.models import Student

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(name=username)
            if check_password(password, user.password):
                request.session['user_id'] = str(user.id)
                match user.role:
                    case 'EMPLOYEE':
                        request.session['employee_id'] = str(user.id)
                        return redirect('employee_home')
                    case 'INSTRUCTOR':
                        request.session['instructor_id'] = str(user.id)
                        return redirect('instructor_home')
                    case 'STUDENT':
                        request.session['student_id'] = str(user.id)
                        return redirect('student_home')
            else:
                messages.error(request, "Incorrect password")
        except User.DoesNotExist:
            messages.error(request, "User not found")
    
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')