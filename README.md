# 📚 Book Store API (Django REST Framework)

A simple Django REST Framework API for managing Authors and Books. It includes token-based authentication, a custom login endpoint, and auto-generated API docs via Swagger and ReDoc.

## ✨ Features

- Django REST Framework for building RESTful APIs
- Token Authentication with a custom login endpoint
- Admin-only access to Book endpoints; Author endpoints are open (demo)
- Pagination (limit/offset) with default page size of 5
- Interactive API docs at `/swagger/` and `/redoc/`
- SQLite for development

## 🧱 Tech Stack

- Python 3.10+
- Django
- Django REST Framework
- drf-yasg (Swagger / ReDoc docs)

## 🚀 Quickstart

1) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Apply migrations and create an admin user

```bash
python manage.py migrate
python manage.py createsuperuser
```

4) Run the development server

```bash
python manage.py runserver
```

- Admin panel: `http://127.0.0.1:8000/admin/`
- API root: `http://127.0.0.1:8000/api/`
- Swagger UI: `http://127.0.0.1:8000/swagger/`
- ReDoc: `http://127.0.0.1:8000/redoc/`

## 🔐 Authentication

This API uses token-based authentication.

- Obtain a token by POSTing credentials to `POST /api/login`
- Include the token in subsequent requests using an `Authorization` header:
  - `Authorization: Token <your_token>`

### Login

```bash
curl -X POST http://127.0.0.1:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "<your_username>", "password": "<your_password>"}'
# {"token": "<token>"}
```

## 🧪 API Endpoints

Base path: `/api/`

- Authors (public for demo):
  - `GET /api/authors/` — list authors
  - `POST /api/authors/` — create author
  - `GET /api/authors/{id}/` — retrieve author
  - `PUT /api/authors/{id}/` — update author
  - `DELETE /api/authors/{id}/` — delete author

- Books (admin-only):
  - `GET /api/books/` — list books
  - `POST /api/books/` — create book
  - `GET /api/books/{id}/` — retrieve book
  - `PUT /api/books/{id}/` — update book
  - `DELETE /api/books/{id}/` — delete book

### Example Requests

- List authors
```bash
curl http://127.0.0.1:8000/api/authors/
```

- Create author
```bash
curl -X POST http://127.0.0.1:8000/api/authors/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Isaac Asimov", "bio": "Science fiction author"}'
```

- List books (requires admin token)
```bash
curl http://127.0.0.1:8000/api/books/ \
  -H "Authorization: Token <token>"
```

- Create book (requires admin token; use an existing `author` id)
```bash
curl -X POST http://127.0.0.1:8000/api/books/ \
  -H "Authorization: Token <token>" \
  -H "Content-Type: application/json" \
  -d '{"title": "Foundation", "description": "Galactic Empire saga", "author": 1}'
```

## 📄 Models

- Author: `name` (str, max 30), `bio` (text)
- Book: `title` (str, max 40), `description` (text), `author` (FK to Author)

## 📜 Documentation (Swagger / ReDoc)

- Swagger UI: `/swagger/`
- ReDoc: `/redoc/`
- Raw schema (JSON/YAML): `/swagger.json` or `/swagger.yaml`

## 🔢 Pagination

Limit/Offset style. Default page size is 5. Use `?limit=` and `?offset=` query params, for example:

```
/api/authors/?limit=10&offset=20
```

## 🧩 Project Structure

```
.
├── manage.py
├── book_store/
│   ├── settings.py        # DRF, token auth, pagination
│   ├── urls.py            # routes: /api/, /api/login, swagger/redoc
│   └── yasg.py            # drf_yasg schema and UI routes
└── store/
    ├── models.py          # Author, Book
    ├── serializers.py     # AuthorSerializer, BookSerializer
    ├── views.py           # AuthorViewSet (open), BookViewSet (admin-only), CustomAuthToken
    └── urls.py            # DRF router for authors/books
```

## ⚙️ Configuration Notes

- `DEBUG` is enabled and `SECRET_KEY` is hard-coded for development only. Do not use these settings in production.
- To deploy: configure environment-specific settings (secret key, database, allowed hosts), switch to PostgreSQL or another production-grade DB, and serve with a proper ASGI/WSGI server.

## 📝 License

No explicit license is provided. If you plan to open-source this project, consider adding a `LICENSE` file. 