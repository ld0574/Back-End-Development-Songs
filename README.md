# Back-End-Development-Songs

This repository contains the Flask Songs microservice for the Back-End Development Capstone project. It was created from the IBM Developer Skills Network template repository for the Songs service and then completed for the Song resource endpoints.

## Environment Setup

The project was initialized from the provided template repository and configured with the included setup script:

```bash
bash ./bin/setup.sh
```

The setup process installs Python 3.9, creates the course virtual environment, and installs the project dependencies from `requirements.txt`.

Expected environment details:

- Python version: `Python 3.9.x`
- Virtual environment name: `backend-songs-venv`
- Setup script: `bin/setup.sh`

After setup, open a new terminal so the virtual environment is active before running the Flask service or tests.

## Running The Service

Run the Songs service with MongoDB connection details:

```bash
MONGODB_SERVICE=localhost MONGODB_USERNAME=root MONGODB_PASSWORD=password flask --app app run --debugger --reload
```

The service can also run locally with the in-memory fallback used for development and tests when MongoDB is unavailable.

## Implemented Endpoints

- `GET /health`
- `GET /count`
- `GET /song`
- `POST /song`
- `GET /song/<id>`
- `PUT /song/<id>`
- `DELETE /song/<id>`

## Testing

Run the test suite:

```bash
python -m pytest
```

The local verification completed successfully with:

```text
tests/test_api.py::test_health PASSED
1 passed
```
