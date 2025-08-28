from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student, ClassRoom, Attendance, Teacher
from .forms import StudentForm
from .forms import TeacherForm 
from .forms import ClassRoomForm
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied







def home(request):
    return render(request, "home.html")

@login_required
def student_list(request):
    teacher = _get_teacher_for_user(request.user)
    if teacher and not (request.user.is_staff or request.user.is_superuser):
        students = Student.objects.filter(classroom__teacher=teacher)
    else:
        students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})


@login_required
def add_student(request):
    teacher = _get_teacher_for_user(request.user)

    # If teacher (non-staff) is adding, limit classroom choices to their classrooms.
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['classroom'].queryset = ClassRoom.objects.filter(teacher=teacher)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['classroom'].queryset = ClassRoom.objects.filter(teacher=teacher)

    return render(request, 'student/add_student.html', {'form': form})


@login_required
def edit_student(request, pk):
    teacher = _get_teacher_for_user(request.user)

    # If teacher -> ensure student belongs to that teacher's classroom
    if teacher and not (request.user.is_staff or request.user.is_superuser):
        student = get_object_or_404(Student, pk=pk, classroom__teacher=teacher)
    else:
        student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['classroom'].queryset = ClassRoom.objects.filter(teacher=teacher)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['classroom'].queryset = ClassRoom.objects.filter(teacher=teacher)

    return render(request, 'student/edit_student.html', {'form': form})


@login_required
def delete_student(request, pk):
    teacher = _get_teacher_for_user(request.user)

    if teacher and not (request.user.is_staff or request.user.is_superuser):
        student = get_object_or_404(Student, pk=pk, classroom__teacher=teacher)
    else:
        student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'student/delete_student.html', {'student': student})


# View to display all Teacher entries using a template


@login_required
def teacher_list(request):
    """Only staff/superusers can see the list of Teachers"""
    if not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})


@login_required
def teacher_create(request):
    """Only staff/superusers can create new Teachers"""
    if not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied
    
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher/teacher_form.html', {'form': form})


@login_required
def teacher_update(request, pk):
    """Only staff/superusers can update Teachers"""
    if not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied
    
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher/teacher_form.html', {'form': form})


@login_required
def teacher_delete(request, pk):
    """Only staff/superusers can delete Teachers"""
    if not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied
    
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teacher/teacher_confirm_delete.html', {'teacher': teacher})

# Helper to fetch Teacher tied to the current user
def _get_teacher_for_user(user):
    from .models import Teacher
    return Teacher._get_teacher_for_user(user)


# View to display all ClassRoom entries using a template
@login_required
def classroom_list(request):
    teacher = _get_teacher_for_user(request.user)
    if teacher and not (request.user.is_staff or request.user.is_superuser):
        classrooms = ClassRoom.objects.filter(teacher=teacher)
    else:
        classrooms = ClassRoom.objects.all()
    return render(request, 'classroom/classroom_list.html', {'classrooms': classrooms})


@login_required
def classroom_create(request):
    # Creating classrooms is usually an admin/staff action.
    if not (request.user.is_staff or request.user.is_superuser):
        raise PermissionDenied

    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
    else:
        form = ClassRoomForm()
    return render(request, 'classroom/classroom_form.html', {'form': form})


@login_required
def classroom_update(request, pk):
    teacher = _get_teacher_for_user(request.user)

    # If teacher (non-staff) updating, ensure they own that classroom
    if teacher and not (request.user.is_staff or request.user.is_superuser):
        classroom = get_object_or_404(ClassRoom, pk=pk, teacher=teacher)
    else:
        classroom = get_object_or_404(ClassRoom, pk=pk)

    if request.method == "POST":
        form = ClassRoomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
    else:
        form = ClassRoomForm(instance=classroom)

    return render(request, 'classroom/classroom_form.html', {'form': form})


@login_required
def classroom_delete(request, pk):
    teacher = _get_teacher_for_user(request.user)

    if teacher and not (request.user.is_staff or request.user.is_superuser):
        classroom = get_object_or_404(ClassRoom, pk=pk, teacher=teacher)
    else:
        classroom = get_object_or_404(ClassRoom, pk=pk)

    if request.method == "POST":
        classroom.delete()
        return redirect('classroom_list')

    return render(request, 'classroom/classroom_confirm_delete.html', {'classroom': classroom})


# View to display all Attendance entries using a template

# View: List all attendance records
@login_required
def attendance_list(request):
    teacher = _get_teacher_for_user(request.user)
    if teacher and not (request.user.is_staff or request.user.is_superuser):
        attendances = Attendance.objects.filter(student__classroom__teacher=teacher).order_by('-date')
    else:
        attendances = Attendance.objects.all().order_by('-date')
    return render(request, 'attendance/attendance_list.html', {'attendances': attendances})


@login_required
def attendance_create(request):
    teacher = _get_teacher_for_user(request.user)

    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['student'].queryset = Student.objects.filter(classroom__teacher=teacher)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['student'].queryset = Student.objects.filter(classroom__teacher=teacher)

    return render(request, 'attendance/attendance_form.html', {'form' : form})


@login_required
def attendance_update(request, pk):
    teacher = _get_teacher_for_user(request.user)

    if teacher and not (request.user.is_staff or request.user.is_superuser):
        attendance = get_object_or_404(Attendance, pk=pk, student__classroom__teacher=teacher)
    else:
        attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['student'].queryset = Student.objects.filter(classroom__teacher=teacher)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=attendance)
        if teacher and not (request.user.is_staff or request.user.is_superuser):
            form.fields['student'].queryset = Student.objects.filter(classroom__teacher=teacher)

    return render(request, 'attendance/attendance_form.html', {'form' : form})


@login_required
def attendance_delete(request, pk):
    teacher = _get_teacher_for_user(request.user)

    if teacher and not (request.user.is_staff or request.user.is_superuser):
        attendance = get_object_or_404(Attendance, pk=pk, student__classroom__teacher=teacher)
    else:
        attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == 'POST':
        attendance.delete()
        return redirect('attendance_list')

    # Fixed: use render, not a tuple
    return render(request, 'attendance/attendance_confirm_delete.html', {'attendance': attendance})


