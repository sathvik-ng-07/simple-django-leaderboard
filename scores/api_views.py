# scores/api_views.py

from rest_framework import generics
from rest_framework.response import Response
from .models import Score
from .serializers import ScoreSerializer, LeaderboardSerializer
from .redis_utils import update_score, get_leaderboard

class SubmitScoreView(generics.CreateAPIView):
    serializer_class = ScoreSerializer

    def perform_create(self, serializer):
        score = serializer.save(user=self.request.user)
        update_score(self.request.user, score.game, score.score)

class LeaderboardView(generics.GenericAPIView):
    serializer_class = LeaderboardSerializer

    def get(self, request, game):
        top_scores = get_leaderboard(game)
        data = [{'username': username, 'score': score} for username, score in top_scores]
        return Response(data)
