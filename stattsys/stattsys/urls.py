from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name = 'add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete-student'),
    path('classrooms/', views.class_room, name="class_room"),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('teachers/', views.teacher, name='teacher_list'),

]


