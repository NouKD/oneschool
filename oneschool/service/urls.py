from django.urls import path
from . import views

urlpatterns = [
    path('cours', views.cours, name='cours'),
    path('programme', views.programme, name='programme'),
    path('teacher', views.teacher, name='teacher'),
]