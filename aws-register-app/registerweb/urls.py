
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reg/', views.register_email, name='register')
]
