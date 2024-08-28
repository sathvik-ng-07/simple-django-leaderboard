# Simple Django Leaderboard

A real-time leaderboard system built with Django and Redis, featuring user authentication, score submissions, live updates, and pagination. This project demonstrates efficient leaderboard management using Redis sorted sets and provides REST API endpoints for easy integration.

## Features

- **User Authentication:** Secure user registration and login.
- **Score Submission:** Users can submit scores for different games or activities.
- **Real-Time Leaderboard:** Displays the top users with live updates.
- **Pagination:** Leaderboard results are paginated for better readability.
- **REST API:** Endpoints for submitting scores and retrieving leaderboard data.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sathvik-ng-07/simple-django-leaderboard.git
   cd simple-django-leaderboard
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Redis:**
   Ensure Redis is installed and running on your machine. You can download and install Redis from [here](https://redis.io/download).

5. **Configure the Django settings:**
   Update your `settings.py` to connect to your Redis instance.

6. **Run the migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

- **Access the leaderboard:** 
  Visit `http://localhost:8000/scores/leaderboard/` to view the leaderboard.
  
- **Submit scores:**
  Use the REST API to submit scores for any game or activity:
  ```bash
  curl -X POST http://localhost:8000/scores/api/submit_score/ -H "Content-Type: application/json" -d '{"game": "your_game_name", "score": your_score}'
  ```

- **Retrieve the leaderboard:**
  Use the REST API to retrieve the leaderboard with pagination:
  ```bash
  curl -X GET http://localhost:8000/scores/api/leaderboard/your_game_name/?page=1
  ```

## Technologies Used

- **Django:** Web framework for the backend.
- **Redis:** In-memory data structure store for managing the leaderboard.
- **Django REST Framework:** For building the REST API.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Project Idea:
https://roadmap.sh/projects/realtime-leaderboard-system
