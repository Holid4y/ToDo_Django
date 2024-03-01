from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.http import JsonResponse
from distutils.util import strtobool

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks': tasks})

def get_tasks(request):
    tasks = Task.objects.all().values('title', 'completed')
    return JsonResponse(list(tasks), safe=False)

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        if title:
            task = Task.objects.create(title=title)
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def delete_task(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        if title:
            Task.objects.filter(title=title).delete()
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def edit_task(request):
    if request.method == 'POST':
        old_title = request.POST.get('old_title', '')
        new_title = request.POST.get('new_title', '')
        if old_title and new_title:
            task = Task.objects.filter(title=old_title).first()
            if task:
                task.title = new_title
                task.save()
                return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def update_task_status(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        completed_str = request.POST.get('completed', '').lower()
        completed = completed_str == 'true'
        if title:
            task = Task.objects.filter(title=title).first()
            if task:
                task.completed = completed
                task.save()
                return JsonResponse({'success': True})
    return JsonResponse({'success': False})