from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('proffs/proff/<str:tc>/', views.proff, name='proff'),
    path('proffs/', views.proffs, name='proffs'),
    path('students/student/<str:st>/', views.student, name='student'),
    path('students/', views.students, name='students'),
    path('teacher_form/', views.teacher_form, name='teacher_form'),
    path('student_form/', views.student_form, name='student_form'),
    path('teacher_update/<str:pk>/', views.teacher_update, name='teacher_update'),
    path('student_update/<str:st>/', views.student_update, name='student_update'),
]