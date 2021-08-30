from django.shortcuts import render

from .models import Question, Answer
from .serializer import RandomQuestionSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from core.quizbot import serializer



class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(is_active=True).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

