from django.shortcuts import render
from datetime import datetime

def home(request):
    context = {
        'name': 'Ishtiyaq Alam',
        'course': 'Django Internship',
        'today': datetime.now(),
        'numbers': [10, 20, 30, 40]
    }

    return render(request, 'home.html', context)


def about(request):
    context = {
        'description': 'This is Django templating practice project.',
        'skills': ['Inheritance', 'Filters', 'Tags']
    }

    return render(request, 'about.html', context)

