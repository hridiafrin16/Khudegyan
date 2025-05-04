from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User
class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('parent', 'Parent'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

# Course
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
#   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField('Student', related_name='course_set')

    def __str__(self):
        return self.title

# Student
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade_level = models.CharField(max_length=20)
    progress_tracking = models.TextField()
    courses = models.ManyToManyField('Course', related_name='enrolled_students')

    def __str__(self):
        return self.user.username

# Teacher
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise_area = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


# Parent
class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    child = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

# Study Material
class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.type}"


# Quiz
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.TextField()
    answer_option = models.TextField()
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.quiz)

# Progress Report
class ProgressReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
    completion_status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.student)
# Gaming Engine
class GamingEngine(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.IntegerField()
    level = models.IntegerField()

    def __str__(self):
        return str(self.student)

class Game(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
