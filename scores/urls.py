from django.urls import path
from . import views
from .api_views import SubmitScoreView, LeaderboardView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('submit/', views.submit_score, name='submit_score'),
    path('leaderboard/<str:game>/', views.leaderboard, name='leaderboard'),
    path('api/submit_score/', SubmitScoreView.as_view(), name='submit_score_api'),
    path('api/leaderboard/<str:game>/', LeaderboardView.as_view(), name='leaderboard_api'),

]
