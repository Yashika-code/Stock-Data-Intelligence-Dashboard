# 📊 Stock Data Intelligence Dashboard

## 👋 About the Project

This project was developed as part of an internship assignment to understand how real-world stock market data can be fetched, processed, stored, and exposed using backend APIs.

The project focuses mainly on **backend development**, data handling, and API design using FastAPI.

---

## 🚀 What This Project Does

* Fetches real stock market data for selected companies (INFY, TCS, RELIANCE) using **yfinance**
* Cleans and processes stock price data using **Pandas**
* Stores processed stock data in a **SQLite database**
* Exposes stock data through **FastAPI-based REST APIs**
* Provides interactive API documentation using **Swagger UI**

> Note: The primary focus of this project is backend functionality. Frontend visualization is minimal.

---

## 🛠 Technologies Used

* **Python**
* **FastAPI** – REST API framework
* **SQLite** – lightweight database
* **Pandas & NumPy** – data processing
* **yfinance** – fetching stock market data

---

## 📁 Project Structure

```
stock-dashboard/
│
├── app/
│   ├── main.py          # FastAPI app and routes
│   ├── database.py      # Database connection
│   ├── models.py        # Database models
│   ├── data_loader.py   # Stock data fetching and cleaning
│   ├── schemas.py       # API response schemas
│
├── frontend/
│   └── index.html       # Basic frontend (optional / minimal)
│
├── requirements.txt
├── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Yashika-code/Stock-Data-Intelligence-Dashboard.git
cd stock-dashboard
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate   # Linux / Mac
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the Server

```bash
uvicorn app.main:app --reload
```

---

## 🔗 API Endpoints

### 📌 Get List of Companies

```
GET /companies
```

Returns the list of supported stock symbols.

---

### 📌 Get Stock Data

```
GET /data/{symbol}
```

Example:

```
/data/INFY
```

Returns recent stock price data for the selected company.

---

### 📌 Get Stock Summary

```
GET /summary/{symbol}
```

Returns:

* 52-week high
* 52-week low
* Average closing price

---

## 📘 API Documentation

FastAPI provides built-in interactive documentation.

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📈 Frontend

A very basic frontend structure is included in the project.
At present, the frontend is **minimal and optional**, and the main interaction with the project is through the backend APIs and Swagger UI.

---

## 🔮 Possible Improvements

* Add advanced metrics like volatility and moving averages
* Stock comparison APIs
* Full frontend dashboard with charts
* Cloud deployment
* Dockerization

---

## ✅ Conclusion

This project helped me gain practical experience with:

* Working with real financial data
* Data cleaning and processing using Pandas
* Designing REST APIs with FastAPI
* Database integration using SQLite

---
