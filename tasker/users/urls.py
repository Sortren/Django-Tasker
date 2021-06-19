from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('reset-stats/', views.reset_stats, name='reset-stats'),
]
