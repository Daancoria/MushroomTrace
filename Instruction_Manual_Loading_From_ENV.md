
# 📚 Instruction Manual: Loading Mushroom App Database Settings from .env File

---

## ✅ Why Use a .env File?

- Securely store sensitive credentials (MySQL, Square API, etc.)
- Avoid hardcoding passwords in your code
- Easily switch between environments (development, production)

---

## 🛠 Prerequisites

- Install `python-dotenv` library:

```bash
pip install python-dotenv
```

- Have a `.env` file configured like this:

```env
DB_HOST=localhost
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=mushroom_traceability

# (Optional) Square settings
SQUARE_ACCESS_TOKEN=your_token
SQUARE_LOCATION_ID=your_location
SQUARE_CUSTOMER_ID=your_customer
SQUARE_ORDER_ID=your_order
USE_MOCK_SQUARE=1
```

---

## 🛠 Updated `database.py` to Load from .env

Create or update `database.py` like this:

```python
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
```

✅ Now your app connects dynamically using your `.env` file.

---

## 🔥 Why This Is Better

| Old | New |
|:----|:----|
| Hardcoded credentials | Dynamic, secure loading |
| Hard to switch users/servers | Easy by changing .env |
| Passwords visible in source code | Passwords hidden |

---

## 📋 Important Notes

- Always **add `.env` to `.gitignore`** to prevent uploading it to GitHub.
- Handle missing environment variables safely if needed (advanced).
- Load `.env` as early as possible in your app (inside `__init__` or `manager.py`).

---

## 🏆 Summary

| Step | Action |
|:-----|:-------|
| Install python-dotenv | `pip install python-dotenv` |
| Create .env file with DB and API settings | ✅ |
| Update database.py to load from environment | ✅ |
| Secure, professional backend ready | ✅ |

---

## 📩 Contact

Built by [Daancoria].
