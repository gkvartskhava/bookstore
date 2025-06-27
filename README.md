
# 📚 Book Store API

This is a Django REST Framework-based backend project for a book store. It includes token authentication, Swagger documentation, and a custom login endpoint. I made this as a homework for Bitcamp (Georgian platform where i learned Django Framework).

## 🚀 Features

- Django REST Framework for API building
- Token Authentication
- Custom login view using `obtain_auth_token`
- Swagger UI for API documentation (`drf_yasg`)
- Pagination enabled (limit-offset)
- SQLite for development
- Separate `store` app for API endpoints

## 📦 Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ⚙️ Environment

Make sure to create a `.env` file for any sensitive configurations like `SECRET_KEY` and database settings (currently hardcoded in `settings.py`).



## 🧪 API Endpoints

### Authentication

- `POST /api/login` – Token-based login (returns token)

### Book Store API

All other endpoints are under `/api/` and are defined in `store.urls`.

## 📃 Swagger Docs

API documentation is available at:

```
/swagger/       (Swagger UI)
/redoc/         (ReDoc UI)
```

## 🧩 Middleware and Settings

- Pagination: 5 items per page
- Token-based auth only (`TokenAuthentication`)
- Default timezone: UTC
- Static files: `static/`



## 🧪 Run the Project

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 🧹 Notes

- Project uses SQLite for development — switch to PostgreSQL or another DB in production.
- Swagger UI enabled via `drf_yasg`.

---

Made with ❤️  Django.