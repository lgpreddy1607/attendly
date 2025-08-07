from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student, ClassRoom, Attendance, Teacher
from .forms import StudentForm
from .forms import TeacherForm 
from .forms import ClassRoomForm






def home(request):
    return HttpResponse("Home Page")


def student_list(request):
    """
    View to display a list of all students using a template.

    - Retrieves all Student objects from the database.
    - Passes the student list to the 'student_list.html' template.
    - Renders and returns the HTML response to the client.
    """
    students = Student.objects.all()  # Fetch all students from the database
    return render(request, 'student_list.html', {'students': students})  # Render the template with context    


# View to handle creating a new student
def add_student(request):
    """
    Renders a form to add a new student. On POST, validates and saves the form.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to list of students after save
    else:
        form = StudentForm()
    
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {'form': form})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})


# View to display all Teacher entries using a template


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})

# Create view

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher/teacher_form.html', {'form': form})

# Update view

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher/teacher_form.html', {'form':form})

# Delete view

def teacher_delete(request,pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teacher/teacher_confirm_delete.html', {'teacher':teacher})


# View to display all ClassRoom entries using a template
def classroom_list(request):
    """
    Renders a list of all classrooms using classroom_list.html template.
    """
    classrooms = ClassRoom.objects.all()
    return render(request, 'classroom/classroom_list.html', {'classrooms': classrooms}) 

def classroom_create(request):
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
    else:
        form = ClassRoomForm()
    return render(request, 'classroom/classroom_form.html', {'form': form})
        
def classroom_update(request, pk):
    classroom = get_object_or_404(ClassRoom, pk=pk)
    if request.method == "POST":
        form = ClassRoomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return redirect('classroom_list')
    else:
        form = ClassRoomForm(instance=classroom)
    return render(request, 'classroom/classroom_form.html', {'form':form})

def classroom_delete(request, pk):
    classroom = get_object_or_404(ClassRoom, pk=pk)
    if request.method == "POST":
        classroom.delete()
        return redirect('classroom_list')
    return render(request, 'classroom/classroom_confirm_delete.html', {'classroom':classroom})





# View to display all Attendance entries using a template
def attendance_list(request):
    """
    Renders a list of all attendance records using attendance_list.html template.
    """
    attendance = Attendance.objects.all()
    return render(request, 'attendance_list.html', {'attendance': attendance})


