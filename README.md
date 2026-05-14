# 🛒 E-Commerce Sales Forecasting System

AI-powered end-to-end sales forecasting platform using Machine Learning, FastAPI, and Streamlit.

---

# 📌 Overview

This project simulates a real-world AI system used by modern e-commerce businesses to predict future sales based on:

- website traffic
- advertising spend
- promotional discount strategy

The system combines:

- Machine Learning
- API Engineering
- Interactive Dashboard
- Data Visualization
- Business Analytics

into one production-style portfolio project.

---

# 🚀 Live Features

✅ Sales Prediction Dashboard  
✅ Machine Learning Forecasting Model  
✅ FastAPI Backend API  
✅ Interactive Streamlit Frontend  
✅ Swagger API Documentation  
✅ Public Deployment using ngrok  
✅ Real-time Prediction Interface  

---

# 🖥️ Dashboard Preview

## Main Dashboard

![Dashboard](e-commerce_dashboard.png)

---

## Prediction Result Example

![Prediction Result](e-commerce_dashboard_after.png)

---

# 💼 Business Problem

Modern e-commerce companies need accurate sales forecasting to support:

- inventory planning
- marketing budget allocation
- revenue optimization
- promotional campaign planning
- operational efficiency

Without forecasting systems, businesses risk:

- overstock inventory
- stock shortages
- inefficient advertising spend
- inaccurate revenue planning

This project demonstrates how AI and machine learning can help businesses make more data-driven operational decisions.

---

# 🎯 Business Impact

This forecasting system can help businesses:

- estimate future sales performance
- optimize advertising spending
- evaluate promotional strategies
- improve operational planning
- support strategic decision-making

The workflow reflects practical business use cases commonly found in:

- e-commerce companies
- retail businesses
- AI analytics teams
- business intelligence departments

---

# 🏗️ System Architecture

mermaid
flowchart LR

A[User Input]
--> B[Streamlit Dashboard]

B --> C[FastAPI Backend]

C --> D[Machine Learning Model]

D --> E[Sales Prediction]

E --> F[Prediction Display]
⚙️ Tech Stack
Machine Learning
Scikit-learn
NumPy
Pandas
Backend
FastAPI
Uvicorn
Frontend
Streamlit
Deployment
ngrok
Visualization
Matplotlib
Seaborn
📊 Model Performance
Prediction vs Actual
Training Loss
Revenue Trend Analysis
🔌 API Documentation

The project includes interactive API documentation using Swagger UI.

Swagger API Example
📦 API Example
Request
POST /predict-sales
{
  "day_index": 30,
  "traffic": 20000,
  "ads_spend": 1000,
  "discount": 10
}
Response
{
  "predicted_sales": 15950
}
🧠 Machine Learning Workflow

The project follows an end-to-end machine learning workflow:

Data Collection
Data Cleaning
Feature Engineering
Model Training
Model Evaluation
API Development
Dashboard Development
Deployment & Public Access
📁 Project Structure
Project Folder Structure
E-Commerce-Sales-Forecasting/
│
├── app/
├── data/
├── model/
├── notebooks/
├── screenshots/
├── src/
├── app.py
├── requirements.txt
└── README.md
🖥️ Server Deployment

The application server was deployed using Streamlit and exposed publicly using ngrok.

Server Running Example
⚡ How To Run
1. Clone Repository
git clone https://github.com/yourusername/ecommerce-sales-forecasting.git
2. Install Dependencies
pip install -r requirements.txt
3. Run FastAPI Backend
uvicorn app:app --reload
4. Run Streamlit Dashboard
streamlit run app.py
5. Run ngrok Deployment
from pyngrok import ngrok

public_url = ngrok.connect(8501)
print(public_url)
📈 Key Features
AI-Powered Forecasting

Uses machine learning to estimate future sales based on business metrics.

Interactive Dashboard

Provides a user-friendly interface for real-time prediction testing.

Production-Style API

Implements FastAPI backend architecture commonly used in real-world ML systems.

Public Deployment

Allows external access through ngrok public URLs.

🧪 Engineering Decisions
Why FastAPI?

FastAPI was selected because:

lightweight
fast inference performance
automatic Swagger documentation
production-friendly architecture
Why Streamlit?

Streamlit enables:

rapid dashboard prototyping
interactive UI development
quick ML visualization
Why ngrok?

ngrok was used to:

expose localhost services publicly
test deployment workflows
simulate real-world API accessibility
⚠️ Current Limitations
model trained on sample dataset
temporary deployment using ngrok
no authentication system implemented yet
no cloud infrastructure integration yet
🔮 Future Improvements

Potential future upgrades include:

Docker containerization
CI/CD pipeline
PostgreSQL integration
cloud deployment (AWS/GCP)
model monitoring
real-time analytics dashboard
advanced forecasting algorithms
MLOps pipeline integration
📚 What I Learned

Through this project, I learned:

machine learning deployment workflows
API engineering using FastAPI
interactive dashboard development
public deployment using ngrok
end-to-end ML system integration
business-oriented AI implementation
production-style project structuring
👨‍💻 Author
Nicolas Gabriel
GitHub
https://github.com/NzxCode
LinkedIn
https://www.linkedin.com/
⭐ Final Notes

This project was built to simulate a real-world AI engineering workflow that combines:

machine learning
backend engineering
frontend dashboard development
deployment workflows
business-oriented analytics

into a single end-to-end production-style portfolio project.
