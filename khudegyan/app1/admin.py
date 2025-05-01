from django.contrib import admin
from .models import *
from .models import Game, GamingEngine

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(StudyMaterial)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(ProgressReport)
admin.site.register(Game)
admin.site.register(GamingEngine)

