from django.shortcuts import redirect
from functools import wraps
from users.models import User

def login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if not user_id or not User.objects.filter(id=user_id).exists():
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def role_required(allowed_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_id = request.session.get('user_id')
            if not user_id or not User.objects.filter(id=user_id).exists():
                return redirect('login')
            user = User.objects.get(id=user_id)
            if user.role != allowed_role:
                return redirect('login')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator