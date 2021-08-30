from core.quizbot import serializer
from django.db.models import F

from .models import Score
from .serializer import ScoreSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status


class UpdateScores(APIView):

    def get(self, request, format=None, **kwargs):
        scores = Score.objects.all().order_by('-points')[:10]
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer._validated_data['name']
            points = serializer._validated_data['points']

            if Score.objects.filter(name=name).exists():
                serializer = Score.objects.get(name=name)
                serializer.points = F('points') + points

            serializer.save()
            return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_100_BAD_REQUEST)
        