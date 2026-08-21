<p align="center">
    <img src="./docs/banner.png" alt="banner"/>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python"/>
    <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI"/>
    <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white" alt="SQLAlchemy"/>
    <img src="https://img.shields.io/badge/Pydantic-E92063?logo=pydantic&logoColor=white" alt="Pydantic"/>
    <img src="https://img.shields.io/badge/Alembic-1F1F1F?logoColor=white" alt="Alembic"/>
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License"/>
</p>

<p align="center">
A library management API built with FastAPI, SQLAlchemy, Pydantic, and Hexagonal Architecture.
</p>

<p align="center">
This project is a practical exercise focused on applying Hexagonal Architecture principles, separating domain logic from application, infrastructure, and presentation concerns.
</p>

---

## Getting Started

### Prerequisites

- Python 3.14+
- Docker (to run PostgreSQL via `docker-compose`)

### 1. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment variables

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

### 3. Start the database

```bash
docker compose up -d
```

This starts a PostgreSQL container using the credentials from your `.env` file.

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Run the API

```bash
python main.py
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

---

## Folder Structure

```txt
/
├── alembic.ini
├── docker-compose.yaml
├── docs
│   └── banner.png
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── src
    ├── application
    │   ├── dto
    │   │   ├── book_dto.py
    │   │   ├── __init__.py
    │   │   ├── loan_dto.py
    │   │   └── user_dto.py
    │   ├── exceptions.py
    │   ├── __init__.py
    │   ├── ports
    │   │   ├── __init__.py
    │   │   ├── repositories
    │   │   │   ├── book_repository.py
    │   │   │   ├── __init__.py
    │   │   │   ├── loan_repository.py
    │   │   │   └── user_repository.py
    │   │   └── services
    │   │       ├── auth_service.py
    │   │       └── __init__.py
    │   └── use_cases
    │       ├── book
    │       │   ├── __init__.py
    │       │   └── list_books_use_case.py
    │       ├── __init__.py
    │       ├── loan
    │       │   ├── __init__.py
    │       │   ├── list_loans_use_case.py
    │       │   ├── make_loan_use_case.py
    │       │   └── return_loan_use_case.py
    │       └── user
    │           ├── __init__.py
    │           ├── login_user_use_case.py
    │           └── register_user_use_case.py
    ├── domain
    │   ├── entities
    │   │   ├── book.py
    │   │   ├── __init__.py
    │   │   └── user.py
    │   ├── __init__.py
    │   └── value_objects
    │       ├── __init__.py
    │       └── loan.py
    ├── infrastructure
    │   ├── config
    │   │   └── settings.py
    │   ├── database
    │   │   ├── models
    │   │   │   ├── book.py
    │   │   │   ├── loan.py
    │   │   │   └── user.py
    │   │   ├── repositories
    │   │   │   ├── book_repository.py
    │   │   │   ├── loan_repository.py
    │   │   │   └── user_repository.py
    │   │   └── session.py
    │   ├── __init__.py
    │   └── jwt
    │       └── services
    │           └── auth_service.py
    ├── __init__.py
    └── presentation
        ├── api
        │   ├── app.py
        │   ├── deps.py
        │   ├── error_handler.py
        │   └── routes
        │       ├── book.py
        │       ├── health.py
        │       ├── loan.py
        │       └── user.py
        └── __init__.py
```

---

## License

This project is licensed under the [MIT License](./LICENSE).

## Author

- [Yenterick](https://github.com/Yenterick)