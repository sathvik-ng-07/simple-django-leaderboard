# scores/serializers.py

from rest_framework import serializers
from .models import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['user', 'game', 'score']

class LeaderboardSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    score = serializers.FloatField()
