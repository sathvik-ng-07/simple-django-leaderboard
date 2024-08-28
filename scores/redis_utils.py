import redis
from django.conf import settings
from django.contrib.auth.models import User

redis_client = redis.StrictRedis.from_url(settings.CACHES['default']['LOCATION'])

def update_score(user, game, score):
    username = user.username
    key = f"leaderboard:{game}"
    redis_client.zadd(key, {username: score})

def get_leaderboard(game, top_n=10):
    key = f"leaderboard:{game}"
    top_scores = redis_client.zrevrange(key, 0, top_n - 1, withscores=True)
    return [(username.decode('utf-8'), score) for username, score in top_scores]
