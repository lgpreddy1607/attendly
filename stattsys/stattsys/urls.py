from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name = 'add_student'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete-student'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.teacher_create, name = 'teacher_create'),
    path('teachers/<int:pk>/edit/', views.teacher_update, name = 'teacher_update'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name = 'teacher_delete'),
    path('classrooms/', views.classroom_list, name="classroom_list"),
    path('classrooms/add/', views.classroom_create, name = 'classroom_add'),
    path('classroom/<int:pk>/edit/', views.classroom_update, name = 'classroom_edit'),
    path('classrooms/<int:pk>delete/', views.classroom_delete, name = 'classroom_delete'),
    path('attendance/', views.attendance_list, name='attendance_list'),
   

]


