# 🚀 Real-Time Crypto Analytics Dashboard (with ML Forecasting)

> **Category:** Data Analytics · Machine Learning  
> **Date:** May 2025  
> **Client:** Self-Initiated (Portfolio Project)

A fully automated cryptocurrency analytics dashboard that unifies **live price tracking**, **historical data analysis**, and **future forecasting** in one interactive platform — powered by Python, MySQL, Facebook Prophet, and Power BI.

---

## 🧠 Problem Statement

> *“I can track current prices… or I can analyze historical trends… or I can run future predictions. But not all in one place — and not automatically.”*

In the high-volatility world of cryptocurrency, insights must be both fast and smart. This project bridges that gap by combining **real-time tracking**, **deep historical context**, and **ML-based forecasting** into a single dashboard — built for traders, analysts, and learners.

---

## 🎯 Objective

To track and predict cryptocurrency prices in real-time using end-to-end automation, smart ETL pipelines, and machine learning.

---

## 🔨 My Approach

**From Idea to Automation:**

- ✅ **Live Tracking** – Real-time data via [CoinGecko API](https://www.coingecko.com) for BTC, ETH, and DOGE (updates every 15 minutes)
- ✅ **Historical Context** – 3+ years of past data stored in a MySQL cloud database
- ✅ **ML Forecasting** – 7-day price prediction using **Facebook Prophet**
- ✅ **Smart Tagging** – Label system to differentiate Live, Historical, and Forecast data
- ✅ **Automation** – Fully automated pipeline with **GitHub Actions** (zero manual work)
- ✅ **Power BI Dashboard** – Dynamic UI with filters for coin, date, and data type

---

## 📊 Why It Matters

This project isn’t just a dashboard — it’s a **real-world solution** that:

- Helps **traders act fast** with real-time price updates  
- Empowers **analysts** to study trends and forecast patterns  
- Teaches **learners** about full-stack data systems — from ingestion to prediction  

> 🔄 **Everything runs automatically. No manual execution required.**

---

## 🌟 Key Features

| Feature                           | Description                                      |
|----------------------------------|--------------------------------------------------|
| 📈 Live Price Tracking            | Auto-refresh every 15 minutes (BTC, ETH, DOGE)   |
| 📅 3+ Years of Historical Data    | Stored in MySQL cloud DB                         |
| 📉 7-Day Forecasting              | Facebook Prophet ML model                        |
| 🔖 Smart Data Tagging             | Tag as `Live`, `Historical`, or `Forecast`       |
| 🔍 Filterable Dashboard           | Filter by coin, date, and data type              |
| 💹 Top Gainers & Losers           | Real-time ranking based on performance           |
| 🧠 Accuracy Tracking              | Forecast error vs actual values                  |
| ☁️ Cloud Deployment               | End-to-end via GitHub Actions                    |

---

## 🧰 Tech Stack

- **Python** (ETL, API handling, automation)
- **MySQL** (Cloud database for storing crypto data)
- **Facebook Prophet** (Time-series forecasting)
- **Flask** (For backend scripts and deployment)
- **Power BI** (Interactive dashboards)
- **GitHub Actions** (CI/CD automation)
- **ChatGPT** (Assisted planning and documentation)

---

## 🧠 Lessons Learned

- ✅ Built a full real-time ETL pipeline from scratch
- ✅ Forecasted in volatile markets using Prophet
- ✅ Handled cloud deployment & automation with GitHub Actions
- ✅ Designed a production-style ML + BI system
- ✅ Learned how to monitor and evaluate prediction accuracy

---

## ⚙️ Installation

> This project assumes you're using a local Python environment. Replace with cloud infra if scaling.

1. **Clone the repository**
   ```bash
   git clone https://github.com/heyvishal08/crypto-tracker-dashboard.git
   cd crypto-dashboard

2. **Install Python Packages**
   ```bash
   pip install -r requirements.txt

3. **Set Environment Variables**
   ```bash
   export DB_HOST="your-db-host"
   export DB_PORT="your-db-port"
   export DB_NAME="your-db-name"
   export DB_USER="your-db-username"
   export DB_PASSWORD="your-db-password"

4. **Run Manually**
   ```bash
   python crypto.py            # To store live data
   python forecast_prices.py   # To generate forecast

## ⚙️ GitHub Actions (Automation)

This repo includes a **.github/workflows/track.yml** workflow to:

- ⏰ Run **crypto.py** every 15 minutes
- 🔮 Run **forecast_prices.py** to insert future prices

## ➕ Set GitHub Secrets

Go to:
Repo → Settings → Secrets → Actions → New Repository Secret

| Secret Name                       | Description                                      |
|----------------------------------|--------------------------------------------------|
| DB_HOST            | MySQL host (e.g. Railway URL)   |
| DB_PORT	    | Usually 3306 or Railway port                         |
| DB_NAME              | Database name                        |
| DB_USER             | Username (e.g. root)       |
| DB_PASSWORD           | Password              |

![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)

