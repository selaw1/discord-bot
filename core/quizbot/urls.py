from django.urls import path

from . import views

app_name = 'quizbot'
urlpatterns = [
    path('', views.RandomQuestion.as_view(), name='random' )
]
