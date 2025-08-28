# stattsys/urls.py  (app-level)
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Students
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.add_student, name="add_student"),
    path("students/<int:pk>/edit/", views.edit_student, name="edit_student"),
    path("students/<int:pk>/delete/", views.delete_student, name="delete_student"),

    # Teachers (staff/superusers only)
    path("teachers/", views.teacher_list, name="teacher_list"),
    path("teachers/add/", views.teacher_create, name="teacher_create"),
    path("teachers/<int:pk>/edit/", views.teacher_update, name="teacher_update"),
    path("teachers/<int:pk>/delete/", views.teacher_delete, name="teacher_delete"),

    # Classrooms
    path("classrooms/", views.classroom_list, name="classroom_list"),
    path("classrooms/add/", views.classroom_create, name="classroom_add"),
    path("classrooms/<int:pk>/edit/", views.classroom_update, name="classroom_edit"),
    path("classrooms/<int:pk>/delete/", views.classroom_delete, name="classroom_delete"),

    # Attendance
    path("attendance/", views.attendance_list, name="attendance_list"),
    path("attendance/add/", views.attendance_create, name="attendance_add"),
    path("attendance/<int:pk>/edit/", views.attendance_update, name="attendance_edit"),
    path("attendance/<int:pk>/delete/", views.attendance_delete, name="attendance_delete"),
]

