# App Module

This folder contains the frontend dashboard and API application logic for the E-Commerce Sales Forecasting System.

---

# Components

## Streamlit Dashboard

Interactive frontend interface used for:

- user input
- sales prediction visualization
- real-time forecasting

---

## FastAPI Backend

Backend API used for:

- receiving prediction requests
- model inference
- returning prediction results

---

# Main Features

- Real-time sales prediction
- Interactive dashboard UI
- REST API integration
- FastAPI Swagger documentation

---

# Technologies Used

- Streamlit
- FastAPI
- Uvicorn
- Python

---

# Application Workflow

mermaid
flowchart LR

A[User Input]
--> B[Dashboard UI]

B --> C[FastAPI API]

C --> D[ML Model]

D --> E[Prediction Result]

# Notes

This module simulates a lightweight production-style machine learning application architecture.
