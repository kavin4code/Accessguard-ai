# AccessGuard AI

A cybersecurity platform that demonstrates, detects, and prevents
**OWASP A01:2025 – Broken Access Control** vulnerabilities.

Built as a phased portfolio project to develop backend development,
security engineering, and software design skills.

---

## Project Goals

| Goal | Description |
|------|-------------|
| Learn Backend Development | Build a production-style API with FastAPI and PostgreSQL |
| Learn Cybersecurity | Implement and defeat Broken Access Control vulnerabilities |
| GitHub Portfolio | Clean, phased, well-documented codebase |
| Resume-Worthy Project | End-to-end security platform with a working dashboard |
| Interview Preparation | Reinforce concepts through hands-on implementation |

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.10 |
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Authentication | JWT (python-jose) |
| Password Hashing | Passlib (bcrypt) |
| Templating | Jinja2 |
| Frontend | Bootstrap 5 |
| Charts | Plotly |
| Config | python-dotenv |
| Testing | pytest |

---

## Project Structure

AccessGuardAI/

├── app/

│   ├── api/            # Route handlers (FastAPI routers)

│   ├── auth/           # Authentication logic

│   ├── core/           # Configuration and shared settings

│   ├── dashboard/      # Dashboard routes and logic

│   ├── database/       # Database connection and session management

│   ├── middleware/      # Custom middleware

│   ├── models/         # SQLAlchemy ORM models

│   ├── schemas/        # Pydantic request/response schemas

│   ├── security/       # Access control and permission logic

│   ├── services/       # Business logic layer

│   └── utils/          # Shared utility functions

├── docs/               # Project documentation

├── static/             # CSS, JS, images

├── templates/          # Jinja2 HTML templates

├── tests/              # pytest test suite

├── main.py             # Application entry point

├── .env                # Local environment variables (not committed)

├── .gitignore

├── README.md

└── requirements.txt

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/AccessGuardAI.git
cd AccessGuardAI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
copy .env .env.example          # Windows
# Edit .env with your values if needed
```

### 5. Start the development server

```bash
uvicorn main:app --reload
```

---

## Verification

| URL | Expected Result |
|-----|-----------------|
| `http://127.0.0.1:8000/` | `{"app":"AccessGuard AI","version":"0.1.0","status":"running"}` |
| `http://127.0.0.1:8000/health` | `{"status":"ok"}` |
| `http://127.0.0.1:8000/docs` | Swagger UI listing both endpoints |

---

## Development Phases

| Phase | Description | Status |
|------:|-------------|:------:|
| 0 | Project skeleton and configuration | ✅ Complete |
| 1 | Database foundation (FastAPI, PostgreSQL & SQLAlchemy setup) | ✅ Complete |
| 2 | Database models (RBAC & Audit Logging) | ✅ Complete |
| 3 | Database migrations (Alembic) | 🔜 Planned |
| 4 | Authentication (JWT & bcrypt) | ⏳ Planned |
| 5 | Role-Based Access Control (RBAC Engine) | ⏳ Planned |
| 6 | Broken Access Control demonstrations | ⏳ Planned |
| 7 | Detection & prevention middleware | ⏳ Planned |
| 8 | Security dashboard | ⏳ Planned |
| 9 | Testing & validation | ⏳ Planned |
| 10 | Deployment & documentation | ⏳ Planned |

---

## Security Focus — OWASP A01:2025

Broken Access Control is the **#1 web application security risk** according to OWASP.
This project implements real vulnerable endpoints, detection middleware, secure
alternatives, and a dashboard to visualise security events.

---

## License

MIT 