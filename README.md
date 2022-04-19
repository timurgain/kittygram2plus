# Kittygram, API-project

## Description

The project provides an API for registering cats and their owners, as well as obtaining data about them.

To access the API, the issue of a token is connected.
Pagination, throttling, permissions are also configured.

## Technologies

- Python 3;
- Django REST Framework;
- SQLlite.

## Installation and launch

Clone repository and navigate to folder on command line::

```
git clone ...
```

```
cd kittygram2plus
```

Create and activate virtual environment:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Install dependencies from requirements.txt file:

```
pip install -r requirements.txt
```

Run migrations:

```
python3 manage.py migrate
```

Launch the project:

```
python3 manage.py runserver
```
