from django.shortcuts import render, redirect
from .forms import TeacherForm
from .forms import StudentForm
from .models import Teacher
from .models import Student

def home(request):
    return render(request, 'home.html')

def proff(request, tc):
    teachers_Obj = None
    for i in Teacher:
        if i['id'] == tc:
            teachers_Obj = i
    context = {'tcs': teachers_Obj}
    return render(request, 'proff.html', context)

def proffs(request):
    profesores = Teacher.objects.all()
    context = {'tcs': profesores}
    return render(request, 'proffs.html', context)

def student(request, st):
    alumn_Obj = None
    for i in Student:
        if i['id'] == st:
            alumn_Obj = i
    context = {'std': alumn_Obj}
    return render(request, 'student.html', context)

def students(request):
    alumnos = Student.objects.all()
    context = {'std': alumnos}
    return render(request, 'students.html', context)

def teacher_form(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proffs')
        
    context = {'form':form}
    return render(request, 'formTeacher.html', context)

def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    context = {'form':form}
    return render(request, 'formStudent.html', context)

def teacher_update(request, pk):
    profesor = Teacher.objects.get(id = pk)
    form = TeacherForm(instance=profesor)
    
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('proffs')

    context = {'form': form}
    
    return render(request, 'formTeacher.html', context)

def student_update(request, st):
    estudiante = Student.objects.get(id = st)
    form = StudentForm(instance=estudiante)
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('students')
        
    context = {'form':form}
    return render(request, 'formStudent.html', context)

def teacher_delete(request, pk):
    profesor = Teacher.objects.get(id=pk)
    
    if request.method == 'POST':
        profesor.delete()
        return redirect('proffs')

    context = {'object': profesor}
    return render(request, 'deleteProffs.html', context)


def student_delete(request, st):
    alumno = Student.objects.get(id = st)
    
    if request.method == 'POST':
        alumno.delete()
        return redirect('students')

    context = {'object': alumno}
    return render(request, 'deleteStudents.html', context)