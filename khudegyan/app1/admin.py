from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(StudyMaterial)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(ProgressReport)
admin.site.register(GamingEngine)

