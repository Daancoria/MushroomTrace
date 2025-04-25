
# 📚 Instruction Manual: Connecting Mushroom Traceability App to MySQL Database

---

## ✅ Overview

This guide explains how to modify the Mushroom Traceability App to save and load delivery logs from a **MySQL database** instead of local JSON files.

You will:

- Connect the app to a MySQL server
- Create a simple database and table
- Update the code to use SQL INSERT and SELECT
- Future-proof for backend expansion

---

## 🛠 Prerequisites

- Python 3.x installed
- MySQL Server installed (local or cloud)
- A MySQL user and password
- Mushroom Traceability App files
- Install MySQL Connector:

```bash
pip install mysql-connector-python
```

---

## 🗄️ Database Setup

### 1. Create a New Database

```sql
CREATE DATABASE mushroom_traceability;
```

### 2. Create a New Table

```sql
USE mushroom_traceability;

CREATE TABLE deliveries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mushroom_type VARCHAR(255),
    box_number INT,
    restaurant_name VARCHAR(255),
    pack_date DATE,
    ship_date DATE
);
```

---

## 🔗 Connecting Python App to MySQL

### 1. Create a `database.py` file

Inside your project, create `database.py` with:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",  # or your server IP
        user="your_mysql_user",
        password="your_mysql_password",
        database="mushroom_traceability"
    )
```

Replace `your_mysql_user` and `your_mysql_password` with your real credentials.

---

## ✍️ Modifying App Logic (example for adding a delivery)

### 2. In `main.py` or `manager.py`, when adding a log:

```python
from database import get_connection

def save_delivery_to_db(mushroom_type, box_number, restaurant, pack_date, ship_date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO deliveries (mushroom_type, box_number, restaurant_name, pack_date, ship_date) "
        "VALUES (%s, %s, %s, %s, %s)",
        (mushroom_type, box_number, restaurant, pack_date, ship_date)
    )
    conn.commit()
    cursor.close()
    conn.close()
```

✅ This replaces saving to `logs.json`.

---

## 🔍 Loading Deliveries from MySQL

```python
def load_deliveries_from_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT mushroom_type, box_number, restaurant_name, pack_date, ship_date FROM deliveries")
    deliveries = cursor.fetchall()
    cursor.close()
    conn.close()

    logs = []
    for d in deliveries:
        log = f"{d[0]} - BOX{d[1]:03d} - {d[2]} - Packed: {d[3]} - Shipped: {d[4]}"
        logs.append(log)
    return logs
```

✅ Then populate `self.logs = load_deliveries_from_db()` inside your app.

---

## 📋 Important Notes

- You no longer need `logs.json` when using SQL
- Exporting to CSV/Excel/PDF still works — just reading data from database
- Always handle connection errors gracefully (optional improvements)

---

## 🎯 Advantages

- Centralized database storage
- Multi-user future-ready (web, mobile expansion)
- No dependency on local file system
- Data backed up automatically if DB managed properly

---

## 🏆 Summary Steps

| Step | Action |
|:-----|:-------|
| Install mysql-connector-python | `pip install mysql-connector-python` |
| Create MySQL database and table | `mushroom_traceability.deliveries` |
| Build `database.py` connector | ✅ |
| Replace local file saves/loads | ✅ |
| Future-proof for API/backend expansion | ✅ |

---

## 📩 Contact

For professional backend upgrades (API, Web dashboards, or cloud deployments), feel free to reach out!


