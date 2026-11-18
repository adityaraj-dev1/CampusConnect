# CampusConnect — Day 1: Project Setup
## day 1:
### What I Did
- Created the project folder structure.
- Created and activated a Python virtual environment.
- Installed project dependencies.
- Created `.env` and `.gitignore`.
- Built the initial FastAPI application.
- Added `/` and `/health` endpoints.
- Tested endpoints using Swagger UI.
- Initialized Git and created the first commit.

### Concepts Learned
1. **Virtual Environment:** Isolates project dependencies from other Python projects.
2. **requirements.txt:** Stores project dependencies so they can be installed elsewhere.
3. **Environment Variables:** Store configuration and sensitive information outside the source code.
4. **.gitignore:** Prevents specified files and folders from being tracked by Git.
5. **FastAPI Application:** `FastAPI()` creates the application instance.
6. **API Routes:** `@app.get()` maps a GET request to a Python function.
7. **Uvicorn:** ASGI server used to run the FastAPI application.
8. **Swagger UI:** Provides an interactive interface to test API endpoints.
9. **Git:** Tracks code changes through commits.

# Day 2: PostgreSQL Integration

### What I Did
- Created the PostgreSQL database `campusconnect_db`.
- Configured the database URL using `.env`.
- Created the SQLAlchemy engine.
- Tested the PostgreSQL connection.
- Created the `SessionLocal` session factory.
- Implemented `get_db()` for session management.
- Connected database sessions to FastAPI using `Depends()`.
- Tested the database session through `/db-check`.

### Concepts Learned
1. **Database URL:** Contains database type, driver, credentials, host, port and database name.
2. **Pydantic Settings:** Loads and validates application configuration from environment variables.
3. **SQLAlchemy Engine:** Manages database connectivity.
4. **Database Session:** Manages database operations and transactions.
5. **Session Factory:** Creates new database sessions when needed.
6. **Commit and Rollback:** Commit saves a transaction; rollback undoes uncommitted changes.
7. **Yield Dependency:** Provides a resource and handles cleanup after its use.
8. **FastAPI Depends():** Injects dependencies into API endpoints.
9. **Session Cleanup:** `db.close()` releases session resources.