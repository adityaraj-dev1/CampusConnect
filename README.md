# CampusConnect

A college placement management system designed to connect students, placement officers and recruiters through a centralized platform.

## Problem Statement

College placement activities are often managed through multiple platforms, making it difficult for students to track job opportunities, applications and interview schedules.

CampusConnect aims to centralize these activities.

## Objectives

- Manage student profiles.
- Publish job opportunities.
- Check student eligibility for jobs.
- Manage job applications.
- Schedule interviews.
- Track placement activities.

## Technology Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

## Current Implementation

- FastAPI application setup.
- Root endpoint (`GET /`).
- Health-check endpoint (`GET /health`).
- Automatic API documentation using Swagger UI.

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
uvicorn app.main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Project Status

Currently under development.