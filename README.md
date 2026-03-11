# API Inspector – Backend

## Overview

The backend of **API Inspector** is built using **Python + Flask** and provides APIs for testing external APIs, performing load testing, storing request history, and generating analytics.

This backend acts as the core engine that executes API requests, measures performance metrics, and stores results in a PostgreSQL database.

---

## Tech Stack

- Python
- Flask
- PostgreSQL (Supabase)
- psycopg2
- concurrent.futures (ThreadPoolExecutor)
- python-dotenv
- requests

---

## Project Structure

backend/
│
├── app.py
│
├── routes
│   ├── request_routes.py
│   ├── loadtest_routes.py
│   ├── history_routes.py
│   └── analytics_routes.py
│
├── services
│   ├── api_tester.py
│   ├── load_tester.py
│   ├── history_service.py
│   └── analytics_service.py
│
├── database
│   └── db.py
│
├── utils
│   └── metrics.py
│
└── .env

---

## Environment Setup

Create a `.env` file inside the backend folder.

Example:

DATABASE_URL=postgresql://user:password@host:5432/database

---

## Install Dependencies

pip install -r requirements.txt

---

## Run the Server

flask --app app run --port 5001

Server will run on:

http://localhost:5000

---

## API Endpoints

### Test API

POST /api/request

Example Request:

{
  "url": "https://api.example.com",
  "method": "GET"
}

Response contains:

- status code
- response body
- response headers
- latency
- response size

---

### Load Test

POST /api/load-test

Example Request:

{
  "url": "https://api.example.com",
  "method": "GET",
  "concurrency": 10,
  "requests_count": 50
}

Returns:

- avg latency
- min latency
- max latency
- success rate
- error rate

Load testing is implemented using **ThreadPoolExecutor** to simulate concurrent API traffic.

---

### Request History

GET /api/history

Returns all previously executed API requests.

DELETE /api/history/<id>

Deletes a specific history record.

---

### Analytics

GET /api/analytics

Returns aggregated metrics such as:

- total requests
- average latency
- success rate
- most tested endpoint

---

## Database

PostgreSQL database hosted using **Supabase**.

Main table used:

requests

Fields:

- id
- url
- method
- status_code
- latency
- response_size
- created_at

---

## Key Technical Decisions

### Modular Architecture
The system separates routes, services, utilities, and database access to improve maintainability.

### Concurrency Handling
Load testing uses **ThreadPoolExecutor** to simulate concurrent requests efficiently.

### Flexible API Execution
All external API requests are handled using `requests.request()` which supports dynamic HTTP methods.

### PostgreSQL Database
PostgreSQL was chosen because it supports strong relational queries and analytics aggregation.

---

## Limitations

- No authentication system implemented
- No rate limiting
- AI analysis endpoint optional

---

## Future Improvements

- AI-based API optimization suggestions
- API collections
- performance dashboards
- advanced metrics such as p95 latency

---

## AI Usage

AI tools were used to assist with:

- system architecture design
- debugging and troubleshooting
- code scaffolding
- documentation
