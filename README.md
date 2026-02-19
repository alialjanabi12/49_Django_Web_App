
# Django Job Application Form

A simple Django web application that collects job application data and stores it in a SQLite database. Submissions can be viewed and managed through the Django Admin panel.

---

## Features

- Job application form with:
  - First Name
  - Last Name
  - Email
  - Available Start Date
  - Current Occupation (radio buttons)
- Saves submissions to SQLite database
- Admin dashboard to view and manage applications
- Bootstrap 5 styling

---

## Tech Stack

- Python 3
- Django
- SQLite
- Bootstrap 5 (CDN)

---

## Project Structure

49_Django_Web_App/
│
├── mysite/              # Django project configuration
├── job_application/     # Main app (models, views, templates, admin)
├── db.sqlite3           # SQLite database
├── manage.py            # Django management file
└── README.md

---

## Setup Instructions (Windows)

### 1. Create Virtual Environment

python -m venv .venv
.\.venv\Scripts\activate

### 2. Install Django

pip install django

### 3. Run Migrations

python manage.py makemigrations
python manage.py migrate

### 4. Create Superuser (Admin)

python manage.py createsuperuser

### 5. Run the Server

python manage.py runserver

Open in browser:
- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

---

## Important Notes

- If you modify models.py, run:
  python manage.py makemigrations
  python manage.py migrate

- If admin throws an error about a missing field (example: lastname),
  check your model's __str__ method and ensure it matches your actual
  field names (example: last_name).

---

## Author

Ali Aljanabi

