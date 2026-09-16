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

### Create and activate a virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure environment variables

### Configure apply existing migrations to build your local database

```bash
python manage.py migrate
```

### Create a superuser for your local db (optional)

```bash
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

The server runs at `http://127.0.0.1:8000/`.

## API Documentation

OpenAPI documentation is generated automatically by
[drf-spectacular](https://drf-spectacular.readthedocs.io/) from the code
(views / serializers), so it stays in sync with the actual API.

With the development server running:

| Path           | Description                                     |
| -------------- | ----------------------------------------------- |
| `/api/docs/`   | Swagger UI (interactive, lets you try requests) |
| `/api/redoc/`  | ReDoc (clean, read-only)                        |
| `/api/schema/` | Raw OpenAPI schema (YAML, for tooling)          |

Example: `http://127.0.0.1:8000/api/docs/`

## Admin Site

The Django admin is used as an internal developer tool (end users interact with
the Next.js frontend, not the admin).

- URL: `http://127.0.0.1:8000/admin/`
- Log in with a superuser account.
