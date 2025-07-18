import json
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import Task
import csv

def index(request):
    tasks = Task.objects.all().order_by('completed', 'due_date', 'priority')
    return render(request, 'todo/index.html', {'tasks': tasks})

@csrf_exempt
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'success': True, 'completed': task.completed})

@csrf_exempt
def edit_task(request, task_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_title = data.get('title', '').strip()
            if not new_title:
                return JsonResponse({'status': 'error', 'message': 'Title cannot be empty.'})
            task = get_object_or_404(Task, pk=task_id)
            task.title = new_title
            task.save()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        due_date = request.POST.get('due_date') or None
        priority = int(request.POST.get('priority', 3))

        task = Task(title=title, priority=priority)
        if due_date:
            task.due_date = due_date
        task.save()
        if task:
            return redirect('index')
    return JsonResponse({'success': False})

@transaction.atomic
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return JsonResponse({'status': 'deleted'})

def export_tasks_csv(request):
    tasks = Task.objects.all().order_by('completed', 'due_date', 'priority')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks-list.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Completed', 'Due Date', 'Priority', 'Created At', 'Updated At'])

    for task in tasks:
        writer.writerow([
            task.title.strip(),
            'Yes' if task.completed else 'No',
            task.due_date.strftime('%d/%m/%Y') if task.due_date else '',
            {1: 'High', 2: 'Medium', 3: 'Low'}.get(task.priority, 'N/A'),
            task.created_at.strftime('%d/%m/%Y %H:%M'),
            task.updated_at.strftime('%d/%m/%Y %H:%M'),
        ])

    return response