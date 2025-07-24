from django.shortcuts import render, redirect
from .models import Assignment
from .forms import AssignmentForm
from django.http import HttpResponseNotFound
import os
from users.decorators import role_required

@role_required('INSTRUCTOR')
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("instructor_assignment")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = AssignmentForm()
    return render(request,"assignments/assignment_create.html",{
        "form":form,
        'title': 'Create Assignment'
    })

@role_required('INSTRUCTOR')
def assignment_update(request,pk):
    assignment = Assignment.objects.filter(pk = pk).first()
    if not assignment:
        return redirect("instructor_assignment")
    
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES,instance = assignment)
        if form.is_valid():
            form.save()
            return redirect("instructor_assignment")
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = AssignmentForm(instance=assignment)
    return render(request,"assignments/assignment_update.html",{"form":form})

@role_required('INSTRUCTOR')
def assignment_delete(request,pk):
    assignment = Assignment.objects.filter(pk = pk).first()
    if not assignment:
        return HttpResponseNotFound("Assignment not found")
    
    if request.method == "POST":
        if assignment.file and os.path.isfile(assignment.file.path):
            os.remove(assignment.file.path)
        assignment.delete()
        return redirect("instructor_assignment")
    return render(request, "assignments/assignment_delete.html", {"assignment": assignment})
