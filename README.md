# python-api-db-integration-framework
# 🔗 Python API & Database Integration Framework

## 🏆 Portfolio Project: Backend Consistency Validation

This project is a **Backend Test Automation Framework** designed to verify **data integrity** between a public REST API and a Relational Database (MySQL).

The main objective is to demonstrate **integration testing** skills, ensuring that data sent via web services is correctly processed and persisted in the data layer.

* **Target API:** [ReqRes.in](https://reqres.in/) (Simulating REST services).
* **Database:** MySQL 8.0 (Containerized in Docker).
* **Focus:** Data Consistency Testing (API vs DB).

***

## 🛠️ Technology Stack

| Tool | Category | Purpose |
| :--- | :--- | :--- |
| **Python 3.x** | Language | Test logic and data handling. |
| **Requests** | HTTP Library | Client for API interaction (GET, POST). |
| **PyMySQL** | Database Driver | Connector for executing SQL queries from Python. |
| **Docker & Compose** | Infrastructure | Deployment of MySQL database in isolated containers. |
| **Pytest** | Runner | Execution of the test suite and assertions. |
| **JSON** | Data | Handling of input and output payloads. |

***

## ⚙️ Framework Architecture

The project follows a modular architecture to separate responsibilities:

```text
python-api-db-integration-framework/
│
├── api_services/       # API Clients (encapsulate endpoints and HTTP methods)
├── db_handlers/        # Database Handlers (connection and SQL execution)
├── config/             # Centralized Configuration (URLs, Credentials)
├── data/               # Static JSON files (Test Payloads)
├── tests/              # Test Scripts (Validation and integration logic)
└── docker-compose.yml  # Infrastructure definition (MySQL)