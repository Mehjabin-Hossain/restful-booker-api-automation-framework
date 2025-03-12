# Restful Booker API Automation Framework

## Project Overview

This project is a beginner-friendly Python API automation framework for the Restful Booker API.
It uses `requests` for HTTP calls, `pytest` for test execution, and `pytest-html` for report generation.

## Tools Used

- Python
- pytest
- requests
- pytest-html
- GitHub Actions

## Folder Structure

- `api/` - Reusable API client modules
  - `auth_api.py`
  - `booking_api.py`
- `tests/` - Pytest test cases
  - `test_auth.py`
  - `test_booking_get.py`
  - `test_booking_create.py`
  - `test_booking_update.py`
  - `test_booking_delete.py`
- `utils/` - Configuration, helpers, payload builders
  - `config.py`
  - `helpers.py`
  - `payloads.py`
- `test_data/` - External test data files
  - `booking_data.json`
- `reports/` - Generated HTML reports
- `.github/workflows/` - GitHub Actions workflow
- `requirements.txt` - Python dependencies
- `pytest.ini` - Pytest configuration
- `README.md` - Project documentation
- `.gitignore` - Ignored files and folders

## Test Scenarios

1. Create auth token
2. Get all booking IDs
3. Get booking by ID
4. Create booking
5. Update booking
6. Partial update booking
7. Delete booking
8. Validate status codes and JSON response bodies
9. Validate key booking fields like `firstname`, `lastname`, `totalprice`, `depositpaid`, and `bookingdates`

## Installation

From the project root in VS Code terminal:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## How to Run Tests

```powershell
pytest
```

## How to Generate HTML Report

```powershell
pytest --html=reports/api_report.html --self-contained-html
```
