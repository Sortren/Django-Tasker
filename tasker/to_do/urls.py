from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='to_do-home'),
    path('login/', views.login, name='to_do-login'),
    path('register/', views.register, name='to_do-register')
]
