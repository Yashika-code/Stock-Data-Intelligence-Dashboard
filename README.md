# 📊 Stock Data Intelligence Dashboard

## 👋 About the Project

This project was built as part of an **internship assignment** to understand how real-world stock market data can be collected, processed, and exposed using APIs.

The main idea was to:

* work with **real stock data**,
* clean and analyze it using Python,
* build **REST APIs**, and
* (optionally) visualize the data in a simple way.

The project focuses more on **backend logic and data handling**, with a lightweight frontend for visualization.

---

## 🚀 What This Project Does

* Fetches real **NSE stock data** (INFY, TCS, RELIANCE) using `yfinance`
* Cleans and processes the data using **Pandas**
* Calculates important stock metrics like:

  * Daily Return
  * 7-day Moving Average
  * 52-week High & Low
  * **Volatility Score (custom metric)**
* Stores processed data in a **SQLite database**
* Provides data through **FastAPI-based REST APIs**
* Includes a simple **HTML + Chart.js dashboard** to visualize stock prices

---

## 🛠 Technologies Used

* **Python**
* **FastAPI** – for building APIs
* **SQLite** – lightweight database
* **Pandas & NumPy** – data processing and calculations
* **yfinance** – fetching stock market data
* **Chart.js** – basic frontend visualization

---

## 📁 Project Structure

```
stock-dashboard/
│
├── app/
│   ├── main.py          # API routes and app logic
│   ├── database.py      # Database connection
│   ├── models.py        # Database schema
│   ├── data_loader.py   # Fetching & cleaning stock data
│   ├── schemas.py       # API response structure
│
├── frontend/
│   └── index.html       # Simple visualization dashboard
│
├── requirements.txt
├── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd stock-dashboard
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate   # Linux / Mac
```

### 3️⃣ Install Required Libraries

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

### 📌 Get Last 30 Days Stock Data

```
GET /data/{symbol}
Example: /data/INFY
```

### 📌 Get Stock Summary

```
GET /summary/{symbol}
```

This returns:

* 52-week High
* 52-week Low
* Average Closing Price
* **Volatility Score**

### 📌 Compare Two Stocks

```
GET /compare?symbol1=INFY&symbol2=TCS
```

---

## 📘 API Documentation

FastAPI automatically provides Swagger documentation.

Open this in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📈 Frontend Dashboard

A basic frontend is included for visualization.

Steps:

1. Open `frontend/index.html` in browser
2. Select a company
3. View the closing price trend on a line chart

The frontend fetches data directly from the backend APIs.

---

## 💡 Custom Metric – Volatility Score

To add some creativity, a **Volatility Score** is calculated using the standard deviation of daily returns.

This helps understand how much a stock price fluctuates and gives a rough idea of risk.

---

## 🔮 Possible Improvements

If extended further, this project can include:

* Cloud deployment (Render / Oracle Cloud)
* Basic ML-based price prediction
* Docker support
* Performance optimizations like caching

---

## ✅ Conclusion

This project helped me understand:

* Working with real financial data
* Data cleaning and analysis using Pandas
* Designing clean REST APIs
* Basic data visualization
