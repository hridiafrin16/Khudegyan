from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Game

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['user', 'grade_level', 'progress_tracking']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'expertise_area']

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['course', 'type', 'content']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['course', 'title']

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['quiz', 'question_text', 'answer_option', 'correct_answer']

class ProgressReportForm(forms.ModelForm):
    class Meta:
        model = ProgressReport
        fields = ['student', 'course', 'score', 'completion_status']

class GamingEngineForm(forms.ModelForm):
    class Meta:
        model = GamingEngine
        fields = ['student', 'score', 'level']

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['user', 'child']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'url']