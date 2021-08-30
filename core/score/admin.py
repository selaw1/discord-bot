from django.contrib import admin

from .models import Score

    
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    fieldsets = [('Score Information', {'fields': ['name','points']})]
    list_display = ['name', 'points']
