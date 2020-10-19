from django.contrib import admin
from users.models import *



@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ["first_name"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_name', 'chapter_name', 'created_on', 'belongs_to']
    search_fields = ["subject_name"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_type', 'detailed_solution']
    search_fields = ["answer_type"]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['complexity', 'q_type', 'question', 'correct_answer', 'subject']
    search_fields = ["complexity"]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'name']
    search_fields = ["first_name"]


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ['score', 'uuid', 'test', 'belongs_to']
    search_fields = ["score"]
