from django import forms
from .models import Student, Teacher, Attendance, ClassRoom

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_no', 'classroom','gender', 'contact']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email','subject']
        