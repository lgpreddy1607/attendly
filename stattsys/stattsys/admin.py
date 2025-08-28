from django.contrib import admin
from .models import Student, ClassRoom, Attendance, Teacher

# Register your models here.

''' Username: guru 
    password: password '''

#admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'gender', 'contact', 'classroom')
    search_fields = ('name', 'roll_no')
    list_filter = ('gender', 'classroom','name')
    ordering = ('roll_no',)


#admin.site.register(ClassRoom)
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher')
    search_fields = ('name', 'teacher')
    list_filter = ('teacher',)


#admin.site.register(Attendance)
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    search_fields = ('student',)
    list_filter = ('status','student')
    ordering = ('date',)


#admin.site.register(Teacher)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject','user')
    search_fields = ('name', 'subject')
    #list_filter = ('name', 'subject')