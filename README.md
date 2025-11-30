# EcoPackAI — Sustainable Packaging Recommendation Platform 
EcoPackAI predicts cost efficiency & carbon footprint of packaging materials and 
recommends optimal eco-friendly options. 
## Features - AI-powered recommendation engine - CO₂ and cost analytics dashboard - Full-stack architecture: Flask, PostgreSQL, Bootstrap, ML models - Deployment-ready cloud architecture 
## Tech Stack 
Python | Flask | PostgreSQL | HTML/CSS/Bootstrap | XGBoost | Random Forest | Plotly | 
GitHub Actions 
 ┌──────────────────┐
 │     Frontend     │
 │ HTML/CSS/JS Form │
 └─────────┬────────┘
           │ User Input
           ▼
 ┌────────────────────┐
 │   Flask Backend    │
 │ (API Endpoints)    │
 └───────┬────────────┘
         │ JSON Request
         ▼
 ┌───────────────────────┐
 │ AI Recommendation     │
 │ Engine (ML Model)     │
 └────────┬──────────────┘
          │ Fetch Material Data
          ▼
 ┌──────────────────────┐
 │ PostgreSQL Database  │
 │ (Sustainability data)│
 └────────┬─────────────┘
          │ Ranked Output
          ▼
 ┌─────────────────────┐
 │  Results UI         │
 │ Recommendations     │
 └────────┬────────────┘
          │ Logs data
          ▼
 ┌──────────────────────┐
 │ BI Dashboard         │
 │ CO₂ & Cost Analytics │
 └──────────────────────┘
