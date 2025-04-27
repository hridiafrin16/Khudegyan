from django.shortcuts import render, redirect
from .models import Course, Student, Teacher, StudyMaterial, Quiz, QuizQuestion, ProgressReport, GamingEngine, Parent
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SignUpForm

def home(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    materials = StudyMaterial.objects.all()
    quizzes = Quiz.objects.all()
    quiz_questions = QuizQuestion.objects.all()
    progress_reports = ProgressReport.objects.all()
    games = GamingEngine.objects.all()
    parents = Parent.objects.all()


    return render(request, 'app1/home.html', {
        'courses': courses,
        'students': students,
        'teachers': teachers,
        'materials': materials,
        'quizzes': quizzes,
        'quiz_questions': quiz_questions,
        'progress_reports': progress_reports,
        'games': games,
        'parents': parents,
    })

# COURSE
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'app1/add_course.html', {'form': form})

# STUDENT
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'app1/add_student.html', {'form': form})

# TEACHER
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'app1/add_teacher.html', {'form': form})

# STUDY MATERIAL
def add_material(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudyMaterialForm()
    return render(request, 'app1/add_material.html', {'form': form})

# QUIZ
def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuizForm()
    return render(request, 'app1/add_quiz.html', {'form': form})

# QUIZ QUESTION
def add_quiz_question(request):
    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuizQuestionForm()
    return render(request, 'app1/add_quiz_question.html', {'form': form})

# PROGRESS REPORT
def add_progress_report(request):
    if request.method == 'POST':
        form = ProgressReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProgressReportForm()
    return render(request, 'app1/add_progress_report.html', {'form': form})

# GAMING ENGINE
def add_game(request):
    if request.method == 'POST':
        form = GamingEngineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GamingEngineForm()
    return render(request, 'app1/add_game.html', {'form': form})

# PARENT
def add_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParentForm()
    return render(request, 'app1/add_parent.html', {'form': form})


# log in
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Go to home after login
        else:
            return render(request, 'app1/login.html', {'error': 'Invalid username or password'})
    return render(request, 'app1/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# HOME PAGE
@login_required
def home(request):
    courses = Course.objects.all()
    return render(request, 'app1/home.html', {'courses': courses})

# ADD TEACHER
@login_required
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TeacherForm()
    return render(request, 'app1/add_teacher.html', {'form': form})

# ADD STUDENT
@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'app1/add_student.html', {'form': form})

# ADD COURSE
@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'app1/add_course.html', {'form': form})

# ADD STUDY MATERIAL
@login_required
def add_material(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudyMaterialForm()
    return render(request, 'app1/add_material.html', {'form': form})

# ADD QUIZ
@login_required
def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuizForm()
    return render(request, 'app1/add_quiz.html', {'form': form})

# ADD QUIZ QUESTION
@login_required
def add_quiz_question(request):
    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = QuizQuestionForm()
    return render(request, 'app1/add_quiz_question.html', {'form': form})

# ADD PROGRESS REPORT
@login_required
def add_progress_report(request):
    if request.method == 'POST':
        form = ProgressReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProgressReportForm()
    return render(request, 'app1/add_progress_report.html', {'form': form})

# ADD GAME (GAMING ENGINE)
@login_required
def add_game(request):
    if request.method == 'POST':
        form = GamingEngineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GamingEngineForm()
    return render(request, 'app1/add_game.html', {'form': form})

# ADD PARENT
@login_required
def add_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ParentForm()
    return render(request, 'app1/add_parent.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after signup go to login page
    else:
        form = SignUpForm()
    return render(request, 'app1/signup.html', {'form': form})