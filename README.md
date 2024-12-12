# Spy Cat Agency API

## Overview

This repository contains the backend code for the **Spy Cat Agency** application. The purpose of the application is to manage spy cats, missions, and targets. It allows the management of spy cats, creating missions with associated targets, assigning cats to missions, and updating mission statuses and target notes.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/boychukmk/SpyCats
   cd SpyCats
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate  # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   Ensure you have a PostgreSQL database setup. Update the database connection string in `app/db/base.py`.
   ```python
   DATABASE_URL = "postgresql://user:password@localhost/spy_cat_agency"
   ```


## Running the Application

1. **Start the application** using Uvicorn:
   ```bash
   uvicorn app.main:app --reload
   ```
   - The application will be running at `http://127.0.0.1:8000/` by default.

2. **Access the Swagger documentation**:
   - You can access the auto-generated Swagger UI at:
     ```
     http://127.0.0.1:8000/docs
     ```
     - This allows you to test the API interactively from the browser.

---

## API Endpoints

Below are the API endpoints for managing spy cats, missions, and targets.

### **1. Spy Cats**

- **Create Spy Cat**
  - **URL**: `POST /cats/`
  - **Request Body**:
    ```json
    {
      "name": "Whiskers",
      "experience_years": 5,
      "breed": "Persian",
      "salary": 50000
    }
    ```
  
- **List All Spy Cats**
  - **URL**: `GET /cats/`
  
- **Get a Single Spy Cat**
  - **URL**: `GET /cats/{cat_id}/`
  
- **Update Spy Cat**
  - **URL**: `PATCH /cats/{cat_id}/`
  - **Request Body**:
    ```json
    {
      "salary": 55000
    }
    ```

- **Delete Spy Cat**
  - **URL**: `DELETE /cats/{cat_id}/`

---

### **2. Missions**

- **Create Mission with Targets**
  - **URL**: `POST /missions/`
  - **Request Body**:
    ```json
    {
      "cat_id": 1,
      "name": "Mission X",
      "targets": [
        {
          "name": "Target 1",
          "country": "USA",
          "notes": "Initial data",
          "complete": false
        },
        {
          "name": "Target 2",
          "country": "Russia",
          "notes": "Pending verification",
          "complete": false
        }
      ]
    }
    ```


- **List All Missions**
  - **URL**: `GET /missions/`

- **Get a Single Mission**
  - **URL**: `GET /missions/{mission_id}/`

- **Update Mission Target**
  - **URL**: `PATCH /missions/{mission_id}/targets/{target_id}/`
  - **Request Body**:
    ```json
    {
      "complete": true,
      "notes": "Data collected"
    }
    ```

- **Delete Mission**
  - **URL**: `DELETE /missions/{mission_id}/`

---

## cURL Examples for API Requests

Here are the cURL commands for every possible request in the application.

### **1. Spy Cats**

- **Create Spy Cat**:
  ```bash
  curl -X 'POST' \
  'http://127.0.0.1:8000/cats/' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Whiskers",
    "years_of_experience": 5,
    "breed": "Persian",
    "salary": 50000.0
  }'

  ```

- **List All Spy Cats**:
  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/cats/'
  ```

- **Get a Single Spy Cat**:
  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/cats/2/'
  ```

- **Update Spy Cat**:
  ```bash
  curl -X 'PATCH' \
    'http://127.0.0.1:8000/cats/2/' \
    -H 'Content-Type: application/json' \
    -d '{
      "salary": 55000
    }'
  ```

- **Delete Spy Cat**:
  ```bash
  curl -X 'DELETE' \
    'http://127.0.0.1:8000/cats/1/'
  ```

---

### **2. Missions**

- **Create Mission with Targets**:
  ```bash
  curl -X 'POST' \
  'http://127.0.0.1:8000/missions/' \
  -H 'Content-Type: application/json' \
  -d '{
    "cat_id": 3,
    "name": "Mission X",
    "targets": [
      {
        "name": "Target 1",
        "country": "USA",
        "notes": "Initial data",
        "complete": false
      },
      {
        "name": "Target 2",
        "country": "Russia",
        "notes": "Pending verification",
        "complete": false
      }
    ]
  }'

  ```


- **List All Missions**:
  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/missions/'
  ```

- **Get a Single Mission**:
  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/missions/1/'
  ```


- **Delete Mission**:
  ```bash
  curl -X 'DELETE' \
    'http://127.0.0.1:8000/missions/1/'
  ```
---
### **3. Targets**

- **Create Target**:
  ```bash
  curl -X 'POST' \
    'http://127.0.0.1:8000/targets/?mission_id=1' \
    -H 'Content-Type: application/json' \
    -d '{
      "name": "Target 1",
      "country": "USA",
      "notes": "Initial notes",
      "complete": false
    }'
  ```

- **Update Target**:
  ```bash
  curl -X 'PATCH' \
    'http://127.0.0.1:8000/targets/1' \
    -H 'Content-Type: application/json' \
    -d '{
      "complete": true,
      "notes": "Updated notes"
    }'
  ```

- **List All Targets**:
  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/targets/'
  ```

- **Get a Single Target**:
  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/targets/1'
  ```

- **Delete Target**:
  ```bash
  curl -X 'DELETE' \
    'http://127.0.0.1:8000/targets/1'
  ```


