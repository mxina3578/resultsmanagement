from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Marks
from .forms import StudentForm, MarksForm
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'main/homepage.html')


def login_view(request):
    role = request.GET.get('role')  # Get role from query params

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user's role matches the requested role
            if (role == 'admin' and getattr(user, 'role', None) == 'admin') or (role == 'student' and getattr(user, 'role', None) == 'student'):
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin_dashboard')
                elif user.role == 'student':
                    return redirect('student_dashboard')
            else:
                # Render a custom error page for mismatched roles
                return render(request, 'main/error.html', {
                    'error': 'You do not have permission to access this role. Please log in with the correct role.'
                })
        else:
            # Render a custom error page for incorrect login credentials
            return render(request, 'main/error.html', {
                'error': 'Invalid username or password. Please try again.'
            })

    return render(request, 'main/login.html', {'role': role})


@login_required
def admin_dashboard(request):
    return render(request, 'main/admin_dashboard.html')


@login_required
def student_dashboard(request):
    return render(request, 'main/student_dashboard.html')


@login_required
def manage_students(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_students')
    else:
        form = StudentForm()
    return render(request, 'main/manage_students.html', {'students': students, 'form': form})


@login_required
def manage_marks(request):
    marks_list = Marks.objects.all()
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_marks')
    else:
        form = MarksForm()
    return render(request, 'main/manage_marks.html', {'marks_list': marks_list, 'form': form})


@login_required
def student_view_marks(request):
    student = get_object_or_404(Student, user=request.user)
    marks = Marks.objects.filter(student=student)
    return render(request, 'main/student_view_marks.html', {'marks': marks})
