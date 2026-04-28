# Contacts API

REST API для зберігання та управління контактами, створений за допомогою FastAPI, SQLAlchemy та PostgreSQL.

## Функціонал

- Створення нового контакту
- Отримання списку всіх контактів
- Отримання контакту за ID
- Оновлення контакту
- Видалення контакту
- Пошук контактів за:
  - ім'ям
  - прізвищем
  - email
- Отримання контактів з днями народження на найближчі 7 днів

---

## Технології

- Python 3.13
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Poetry
- Docker
- Pydantic

---

## Запуск через Docker

### Клонувати репозиторій

```bash
git clone <your_repo_url>
cd goit-pythonweb-hw-08
```

### Запустити контейнери

```bash
docker-compose up --build
```

API буде доступне:

```bash
http://localhost:8000
```

Swagger документація:

```bash
http://localhost:8000/docs
```

---

## Структура проєкту

```bash
app/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── crud.py
│
└── routes/
    └── contacts.py

alembic/
docker-compose.yml
Dockerfile
pyproject.toml
README.md
```

---

## API Endpoints

### Контакти

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/contacts/`     | Create contact    |
| GET    | `/contacts/`     | Get all contacts  |
| GET    | `/contacts/{id}` | Get contact by id |
| PUT    | `/contacts/{id}` | Update contact    |
| DELETE | `/contacts/{id}` | Delete contact    |

---

### Search

```bash
GET /contacts/search?q=oleh
```

---

### Upcoming birthdays

```bash
GET /contacts/birthdays/upcoming
```

---

## Автор

Oleh Fedorchuk
