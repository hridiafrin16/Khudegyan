from django.shortcuts import render
from .models import Course, Student, Teacher, StudyMaterial, Quiz, QuizQuestion, ProgressReport, GamingEngine, Parent


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

    return render(request, 'home.html', {
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
