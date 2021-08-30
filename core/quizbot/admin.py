from django.contrib import admin

from .models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = ['answer', 'is_correct']
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('Question Information', {'fields': ['title','points', 'difficulty', 'is_active']})]
    list_display = ['title', 'difficulty', 'is_active', 'created_at', 'updated_at']
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fieldsets = [('Answer Information', {'fields': ['question','answer', 'is_correct', 'is_active']})]
    list_display = ['answer', 'is_correct', 'is_active', 'created_at', 'updated_at']
