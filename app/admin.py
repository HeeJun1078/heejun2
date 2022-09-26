from django.contrib import admin
from .models import Question, Choice


class QuestionAdminView(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['question_text']


class ChoiceAdminView(admin.ModelAdmin):
    readonly_fields = ('id', )
    list_display = ['choice_text']


admin.site.register(Question, QuestionAdminView)
admin.site.register(Choice, ChoiceAdminView)
# Register your models here.
