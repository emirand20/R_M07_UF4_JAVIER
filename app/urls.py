from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('proffs/proff/<str:tc>/', views.proff, name='proff'),
    path('proffs/', views.proffs, name='proffs'),
    path('students/student/<str:st>/', views.student, name='student'),
    path('students/', views.students, name='students'),
]