from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

@csrf_exempt
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'success': True, 'completed': task.completed})

@csrf_exempt
def update_task(request, task_id):
    new_title = request.POST.get('title')
    task = Task.objects.get(id=task_id)
    task.title = new_title
    task.save()
    return JsonResponse({'success': True, 'title': task.title})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task = Task.objects.create(title=title)
            return redirect('index')
    return JsonResponse({'success': False})

def delete_task(request, task_id):
    Task.objects.filter(id=task_id).delete()
    return JsonResponse({'success': True})
