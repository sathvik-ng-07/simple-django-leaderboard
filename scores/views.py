from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ScoreForm
from .redis_utils import update_score
from .redis_utils import get_leaderboard

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Change to your home page
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})
    return render(request, 'registration/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def submit_score(request):
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            score = form.save(commit=False)
            score.user = request.user
            score.save()
            
            # Update Redis leaderboard
            update_score(request.user, score.game, score.score)
            
            return redirect('home')
    else:
        form = ScoreForm()
    return render(request, 'scores/submit_score.html', {'form': form})

def leaderboard(request, game):
    top_scores = get_leaderboard(game)
    return render(request, 'scores/leaderboard.html', {'game': game, 'top_scores': top_scores})