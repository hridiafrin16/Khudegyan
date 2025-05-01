from django.shortcuts import render, redirect
from .models import Course, Student, Teacher, StudyMaterial, Quiz, QuizQuestion, ProgressReport, GamingEngine, Parent
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import SignUpForm
from django.http import HttpResponseForbidden
from .forms import CourseForm


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
@login_required
def add_course(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can access this page.")

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user
            course.save()
            return redirect('course_list')
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

# Courses Page
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'app1/course_list.html', {'courses': courses})

# Teachers Page
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'app1/teacher_list.html', {'teachers': teachers})

# Quizzes Page
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'app1/quiz_list.html', {'quizzes': quizzes})


#dashboard
def dashboard_view(request):
    if request.user.role == 'teacher':
        return render(request, 'app1/teacher_dashboard.html')
    elif request.user.role == 'student':
        return render(request, 'app1/student_dashboard.html')
    elif request.user.role == 'parent':
        return render(request, 'app1/parent_dashboard.html')
    else:
        return redirect('home')
@login_required
def register_course_view(request):
    courses = Course.objects.all()
    return render(request, 'app1/course_register.html', {'courses':courses})

@login_required
def view_study_material_view(request):
    student = Student.objects.get(user=request.user)
    materials = StudyMaterial.objects.filter(course__student=student)
    return render(request, 'app1/view_study_material.html', {'materials':materials})

@login_required
def solve_quiz_view(request):
    quizzes = Quiz.objects.all()
 # For simplicity, show all questions for now
    questions = QuizQuestion.objects.all()
    return render(request, 'app1/solve_quiz.html', {
    'quiz': quizzes.first(),
    'questions': questions,
    })

@login_required
def view_progress_report_view(request):
    student = Student.objects.get(user=request.user)
    reports = ProgressReport.objects.filter(student=student)
    return render(request, 'app1/view_progress_report.html', {'reports':reports})

@login_required
def view_child_courses_view(request):
    parent = Parent.objects.get(user=request.user)
    student = parent.child
    courses = Course.objects.filter(student=student)
    return render(request, 'app1/view_child_courses.html', {'courses':courses})

@login_required
def view_child_progress_view(request):
    parent = Parent.objects.get(user=request.user)
    student = parent.child
    reports = ProgressReport.objects.filter(student=student)
    return render(request, 'app1/view_child_progress.html', {'reports':reports})

@login_required
def update_material_view(request):
    teacher = Teacher.objects.get(user=request.user)
    courses = Course.objects.filter(created_by=request.user)
    materials = StudyMaterial.objects.filter(course__in=courses)
    return render(request, 'app1/update_material.html', {'materials':materials})

@login_required
def add_quiz_question_view(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id')
        question = request.POST.get('question_text')
        options = request.POST.get('answer_option')
        correct = request.POST.get('correct_answer')

        QuizQuestion.objects.create(
            quiz_id=quiz_id,
            question_text=question,
            answer_option=options,
            correct_answer=correct,
        )
        return redirect('add_quiz_question_page')

    quizzes = Quiz.objects.filter(course__created_by=request.user)
    return render(request, 'app1/add_quiz_question.html', {'quizzes':quizzes})

@login_required
def update_progress_view(request):
    teacher = Teacher.objects.get(user=request.user)
    courses = Course.objects.filter(created_by=request.user)
    students = Student.objects.filter(user_studentcourse_in=courses)

    reports = ProgressReport.objects.filter(course__in=courses)
    return render(request, 'app1/update_progress.html', {'reports':reports})

def dashboard(request):
    if request.user.role == 'teacher':
        return render(request, 'app1/teacher_dashboard.html')
    elif request.user.role == 'student':
        return render(request, 'app1/student_dashboard.html')
    elif request.user.role == 'parent':
        return render(request, 'app1/parent_dashboard.html')
    else:
        return redirect('home')

@login_required
def register_course_view(request):
    courses = Course.objects.all()
    return render(request, 'app1/course_register.html', {'courses':courses})

@login_required
def view_study_material_view(request):
    student = Student.objects.get(user=request.user)
    materials = StudyMaterial.objects.filter(course__student=student)
    return render(request, 'app1/view_study_material.html', {'materials':materials})

@login_required
def solve_quiz_view(request):
    quizzes = Quiz.objects.all()
    # For simplicity, show all questions for now
    questions = QuizQuestion.objects.all()
    return render(request, 'app1/solve_quiz.html', {
        'quiz': quizzes.first(),
        'questions': questions,
})

@login_required
def view_progress_report_view(request):
    student = Student.objects.get(user=request.user)
    reports = ProgressReport.objects.filter(student=student)
    return render(request, 'app1/view_progress_report.html', {'reports':reports})

@login_required
def view_child_courses_view(request):
    parent = Parent.objects.get(user=request.user)
    student = parent.child
    courses = Course.objects.filter(student=student)
    return render(request, 'app1/view_child_courses.html', {'courses':courses})

@login_required
def view_child_progress_view(request):
    parent = Parent.objects.get(user=request.user)
    student = parent.child
    reports = ProgressReport.objects.filter(student=student)
    return render(request, 'app1/view_child_progress.html', {'reports':reports})

@login_required
def update_material_view(request):
    teacher = Teacher.objects.get(user=request.user)
    courses = Course.objects.filter(created_by=request.user)
    materials = StudyMaterial.objects.filter(course__in=courses)
    return render(request, 'app1/update_material.html', {'materials':materials})

@login_required
def add_quiz_question_view(request):
    if request.method == 'POST':
        quiz_id = request.POST.get('quiz_id')
        question = request.POST.get('question_text')
        options = request.POST.get('answer_option')
        correct = request.POST.get('correct_answer')

        QuizQuestion.objects.create(
            quiz_id=quiz_id,
            question_text=question,
            answer_option=options,
            correct_answer=correct,
        )
        return redirect('add_quiz_question_page')

    quizzes = Quiz.objects.filter(course__created_by=request.user)
    return render(request, 'app1/add_quiz_question.html', {'quizzes':quizzes})


@login_required
def update_progress_view(request):
    teacher = Teacher.objects.get(user=request.user)
    courses = Course.objects.filter(created_by=request.user)
    students = Student.objects.filter(user_studentcourse_in=courses)

    reports = ProgressReport.objects.filter(course__in=courses)
    return render(request, 'app1/update_progress.html', {'reports':reports})

@login_required
def update_course(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can update a course.")

    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'app1/update_course.html', {'form': form})


@login_required
def delete_course(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can delete a course.")

    course = Course.objects.get(id=pk)
    course.delete()
    return redirect('course_list')


@login_required
def add_game(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can add games.")

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.added_by = request.user
            game.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'app1/add_game.html', {'form': form})


@login_required
def game_list(request):
    if request.user.role != 'student' and not request.user.is_superuser:
        return HttpResponseForbidden("Access denied.")
    games = Game.objects.all()
    return render(request, 'app1/game_list.html', {'games': games})






