from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='to_do-test'),
    path('login/', views.login, name='to_do-login'),
    path('register/', views.register, name='to_do-register')
]
