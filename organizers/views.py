from django.shortcuts import render, redirect
from .models import Category, Tag
from .forms import CategoryForm, TagForm
from users.decorators import role_required

#Category
@role_required('EMPLOYEE')
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_organizer")
    return render(request,"categories/category_create.html",{"form":form})

@role_required('EMPLOYEE')
def category_update(request,pk):
    category = Category.objects.filter(pk = pk).first()
    form = CategoryForm(request.POST or None,instance = category)
    if form.is_valid():
        form.save()
        return redirect("employee_organizer")
    return render(request,"categories/category_update.html",{"form":form})

@role_required('EMPLOYEE')
def category_delete(request,pk):
    category = Category.objects.filter(pk = pk).first()
    if request.method == "POST":
        category.delete()
        return redirect("employee_organizer")
    return render(request,"categories/category_delete.html",{"category":category})

#Tags
@role_required('EMPLOYEE')
def tag_create(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("employee_organizer")
    return render(request,"tags/tag_create.html",{"form":form})

@role_required('EMPLOYEE')
def tag_update(request,pk):
    tag = Tag.objects.filter(pk = pk).first()
    form = TagForm(request.POST or None,instance = tag)
    if form.is_valid():
        form.save()
        return redirect("employee_organizer")
    return render(request,"tags/tag_update.html",{"form":form})

@role_required('EMPLOYEE')
def tag_delete(request,pk):
    tag = Tag.objects.filter(pk = pk).first()
    if request.method == "POST":
        tag.delete()
        return redirect("employee_organizer")
    return render(request,"tags/tag_delete.html",{"tag":tag})