# judgeServer

Backend service for the `judgeBoy` project, built with Django.

## Tech Stack

- Python 3.12+
- Django 5.2.17
- SQLite3

## Project Structure

```
judgeServer/
   ├── manage.py                    # Django CLI entry point
   ├── config/                      # project package
   │   ├── __init__.py
   │   ├── settings.py
   │   ├── urls.py                  # root URLconf
   │   ├── asgi.py
   │   └── wsgi.py
   └── apps/                        # container for apps
```

## Requirements

- Python 3.12+
- pip / venv

## Setup

1. Create and activate a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies (no `requirements.txt` yet, install Django manually for now)

   ```bash
   pip install django
   ```

3. Run database migrations

   ```bash
   python manage.py migrate
   ```

4. Start the development server

   ```bash
   python manage.py runserver
   ```
