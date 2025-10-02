# Personalized Workout API

A Django REST Framework API for creating and managing personalized workout plans. 
Users can create workouts, track fitness goals, and manage their own workout plans. 
Built with Docker for easy setup and development.

---

## Features

* User registration and authentication
* CRUD for workouts and workout plans
* Only owners can access and modify their own data
* Admin-only access for creating/updating/deleting exercises
* Object-level permissions for secure API access
* Easily deployable with Docker

---

## Prerequisites

* Docker >= 20.x
* Docker Compose >= 2.x
* Git

---

## 1. Clone the repository

```bash
git clone https://github.com/ikamania/personalized-workout-api.git
cd personalized-workout-api
```

---

## 2. Set up environment variables

1. Copy the template `.env` file:

```bash
cp example.env backend/.env
```

2. Edit `backend/.env` with your own values:

```env
DEBUG=True
SECRET_KEY="yoursupersecretkey"
PYTHONUNBUFFERED=1
TZ=UTC
```

---

## 3. Build and run the Docker containers

```bash
docker-compose up --build
```

* The backend will run at `http://0.0.0.0:8000/`.

---

## 4. Apply migrations

```bash
docker-compose exec backend uv run python manage.py migrate
```

* Sets up the database tables.

---

## 5. Create a superuser (admin)

```bash
docker-compose exec backend uv run python manage.py createsuperuser
```

* Follow prompts to set username, email, and password.
* Admin can manage exercises in the Django admin panel.

---

---

## 6. API Endpoints

| Endpoint          | Method | Description                   |
| ----------------- | ------ | ----------------------------- |
| `/users/`         | GET    | List users (only self)        |
| `/users/`         | POST   | Create a new user             |
| `/workouts/`      | GET    | List workouts (only own)      |
| `/workouts/`      | POST   | Create a workout              |
| `/workout-plans/` | GET    | List workout plans (only own) |
| `/workout-plans/` | POST   | Create a workout plan         |
| `/exercises/`     | GET    | List exercises                |
| `/exercises/`     | POST   | Admin only: create exercises  |

> Swagger/OpenAPI docs available at `/swagger/`.

---

## 7. Stop the containers

```bash
docker-compose down
```

---

## 8. Tips

* To reset the database:

```bash
docker-compose exec backend rm db.sqlite3

docker-compose exec backend uv run python manage.py makemigrations
docker-compose exec backend uv run python manage.py migrate
```

* To load initial exercises

```bash
docker-compose exec backend uv run python manage.py load_workouts
```
