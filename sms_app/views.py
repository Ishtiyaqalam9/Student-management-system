from django.shortcuts import render, redirect
from datetime import datetime
from .models import Todo

def home(request):
    if request.method == "POST":
        task = request.POST.get('task')

        if task:
            Todo.objects.create(title=task)

        return redirect('home')

    tasks = Todo.objects.all().order_by('-id')

    context = {
        'name': 'Ishtiyaq Alam',
        'course': 'Django Internship',
        'today': datetime.now(),
        'numbers': [10, 20, 30, 40],
        'tasks': tasks
    }

    return render(request, 'home.html', context)


def about(request):
    context = {
        'description': 'This is Django templating practice project.',
        'skills': ['Inheritance', 'Filters', 'Tags']
    }

    return render(request, 'about.html', context)


def delete_task(request, task_id):
    Todo.objects.filter(id=task_id).delete()
    return redirect('home')