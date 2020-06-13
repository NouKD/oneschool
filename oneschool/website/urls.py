from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('course_single', views.course_single, name='course_single'),
    path('contact', views.index, name='contact'),
]