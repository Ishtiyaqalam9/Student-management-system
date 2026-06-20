from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<int:task_id>/' ,  views.delete_task, name= 'delete_task'),
]