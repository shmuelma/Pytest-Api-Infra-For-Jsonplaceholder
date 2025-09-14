# API Test Automation Framework (pytest + Python)

##  How to Run

1. **Setup environment**

```bash
python -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt
```

2. **Run tests (default: dev)**

```bash
pytest --env=dev
```

3. **Run on production environment**

```bash
pytest --env=prod
```

4. **Run only smoke tests**

```bash
pytest --env=prod -k smoke
```



---

## Project Structure
The name of the commit is Yishai because that is the user the computer was working on.
```
pytest-api-infra/
├── config/        # Environment configs (.env files, config loader)
├── consts/        # Constants and sample mocks (URLs, test data)
├── services/      # Business logic for API endpoints
├── utils/         # Shared helpers (HTTP client, etc.)
├── tests/         # Pytest test files
├── conftest.py    # Fixtures (env, services, http client)
├── pytest.ini     # Pytest markers & settings
└── requirements.txt
```

### Key points:

* **config/** → loads environment variables (e.g. HOSTNAME) from `.env` files.
* **consts/** → defines test URLs and mock data.
* **services/** → wrappers for API endpoints (clean logic, return dict/list only).
* **utils/** → reusable helper modules (HTTP client with retries).
* **tests/** → only contain assertions, no API logic.
* **conftest.py** → central pytest configuration and fixtures.

---



## Features

* Configurable environments via `.env` files.
* Clean separation of API logic (services) and test logic (pytest).
* Support for soft assertions via `pytest-check`.
* Custom pytest markers: `@pytest.mark.smoke`, `@pytest.mark.params`.

---

## Next Steps (Optional Enhancements)

* Add **Allure reporting** for rich test reports.
* Add **CI/CD pipeline** (GitHub Actions or Jenkins).
* Add **requests-mock/vcrpy** for offline tests.
* Add **Pydantic models** for response validation.
