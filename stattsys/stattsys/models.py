from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
    @staticmethod
    def _get_teacher_for_user(user):
        """ Return the Teacher object tied to this User, or None """
        return getattr(user, 'teacher', None)


class ClassRoom(models.Model):
    name = models.CharField(max_length=100)  # Example: "10-A"
    section = models.CharField(max_length=20, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=15, blank=True, null=True)
    classroom = models.ForeignKey(ClassRoom, on_delete = models.SET_NULL, related_name='students', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Leave'),
    ]

    student = models.ForeignKey(Student, on_delete=models.SET_NULL, related_name='attendances', null=True)
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'date')  # Prevent double entry for same date

    def __str__(self):
        return f"{self.date} - {self.student.name} - {self.get_status_display()}"