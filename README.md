
# 🍄 Mushroom Traceability App

A Python desktop application for tracking mushroom deliveries, generating invoices, exporting reports, and managing backup logs. Built with `tkinter`, `ttkbootstrap`, and `docx`, with features like search, filter, PDF/Excel export, summary reports, and custom settings.

---

## ✅ Features

- Track mushroom deliveries (mushroom type, box number, restaurant, pack/ship dates)
- Export to **CSV**, **Excel**, or **PDF**
- Generate **invoices** and **summary reports**
- Live **search** and **date filtering**
- Edit logs individually (delete one entry)
- Settings page with:
  - Default restaurant ID
  - Invoice template path
  - Export folder path
  - Preferred export format
  - Logo path (used in reports)
- Backup system:
  - Auto-backups before clearing logs
  - Backup Manager to restore or delete logs
- Notification toasts for success/errors
- Light/Dark mode support
- Converts to `.exe` for easy distribution
- Live Square API integration (optional)

---

## 📦 Project Structure

```text
MushroomTrace/
│
├── main.py                 # Main GUI + app logic
├── manager.py              # Core logic for invoice/report generation
├── config.py               # Constants for mushrooms/restaurants/settings
├── settings.json           # Saved user preferences
├── traceability_logs.txt   # Optional log file
├── backups/                # Auto-generated backups
├── logo.png                # (Optional) User logo used in reports
└── invoice_template.docx   # (Optional) Branded invoice format
```

---

## ⚙ How the App Works

1. **Add Delivery Entry**: User selects mushroom type, box number, restaurant ID, and dates.
2. **Save/Load Logs**: Logs are saved to `logs.json` and can be reloaded.
3. **Export Options**: Based on Settings (`csv`, `excel`, `pdf`, or all):
   - `Export Data` generates a file named `traceability_log_YYYY-MM-DD.xxx`
   - `Generate Invoice` creates a PDF for the most recent log
   - `Export Summary Report` creates a PDF with delivery stats + table
4. **Backups**: Before clearing all logs, app creates a `.json` backup in `/backups/`
5. **Restore/Delete Backups**: Launch the **Backup Manager** from the UI
6. **Edit Logs**: Delete a specific delivery from the log list

---

## 🛠 How to Convert to `.exe` using PyInstaller

### 1. Install PyInstaller

```bash
pip install pyinstaller
```

### 2. Navigate to the project folder

```bash
cd path/to/MushroomTrace
```

### 3. Build the executable

```bash
pyinstaller main.py --noconfirm --onefile --windowed --icon=logo.ico
```

> 💡 Omit `--icon=logo.ico` if you don’t have a `.ico` file.

### 4. Output

Final `.exe` is created in:

```text
/dist/main.exe
```

You can now share or run the app without Python installed.

---

## 🔑 Tips

- For logos to show in PDF: use `os.path.abspath()` and valid `.png/.jpg`
- Use `Pillow` for image resizing: `pip install pillow`
- Ensure `docx2pdf` is installed and MS Word is available for PDF conversion
- You can center logos, resize automatically, and insert branding

---

## 🧾 Using Square API (Live Mode)

The app is built to support Square invoice integration. You can enable **live Square API** with your real credentials.

### 1. Create a Square Developer Account
Visit: [https://developer.squareup.com](https://developer.squareup.com)  
Create a new application to obtain:

- **Access Token**
- **Location ID**
- **Customer ID**
- **Order ID** (optional if generating manually)

### 2. Set Your Environment Variables

Before running the app, define these:

```bash
set SQUARE_ACCESS_TOKEN=your_real_access_token
set SQUARE_LOCATION_ID=your_location_id
set SQUARE_CUSTOMER_ID=your_customer_id
set SQUARE_ORDER_ID=your_order_id
set USE_MOCK_SQUARE=0
```

Or on Unix/macOS:

```bash
export SQUARE_ACCESS_TOKEN=your_real_access_token
export SQUARE_LOCATION_ID=your_location_id
export SQUARE_CUSTOMER_ID=your_customer_id
export SQUARE_ORDER_ID=your_order_id
export USE_MOCK_SQUARE=0
```

This disables the mock mode and allows the app to connect to real Square services to generate invoices.

> 💡 You can also manually set these in a `.env` file and load with Python `dotenv` if you prefer.

### 3. Toggle Between Modes

You can switch between **Mock** and **Live** at runtime from the UI using the “Toggle Mock/Live Mode” button.

- `USE_MOCK_SQUARE=1` → Fake (for testing)
- `USE_MOCK_SQUARE=0` → Real Square API

---
