from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='to_do-home'),
    path('add-task/', views.add_task, name="add-task")
]
