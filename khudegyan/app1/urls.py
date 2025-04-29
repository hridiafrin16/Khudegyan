"""
URL configuration for khudegyan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', views.home, name='home'),
path('add-course/', add_course, name='add_course'),
    path('add-student/', add_student, name='add_student'),
    path('add-teacher/', add_teacher, name='add_teacher'),
    path('add-material/', add_material, name='add_material'),
    path('add-quiz/', add_quiz, name='add_quiz'),
    path('add-quiz-question/', add_quiz_question, name='add_quiz_question'),
    path('add-progress-report/', add_progress_report, name='add_progress_report'),
    path('add-game/', add_game, name='add_game'),
    path('add-parent/', add_parent, name='add_parent'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


path('signup/', signup_view, name='signup'),

path('courses/', course_list, name='course_list'),
path('teachers/', teacher_list, name='teacher_list'),
path('quizzes/', quiz_list, name='quiz_list'),

# Dashboards
path('dashboard/', dashboard_view, name='dashboard'),  # common dashboard to redirect by role

# Teacher Actions
path('update-material/', update_material_view, name='update_material_page'),
path('add-quiz-question/', add_quiz_question_view, name='add_quiz_question_page'),
path('update-progress/', update_progress_view, name='update_progress_page'),

# Student Actions
path('register-course/', register_course_view, name='course_register_page'),
path('view-materials/', view_study_material_view, name='view_study_material_page'),
path('solve-quiz/', solve_quiz_view, name='solve_quiz_page'),
path('view-progress/', view_progress_report_view, name='view_progress_report_page'),

# Parent Actions
path('view-child-progress/', view_child_progress_view, name='view_child_progress_page'),
path('view-child-courses/', view_child_courses_view, name='view_child_courses_page'),



]
