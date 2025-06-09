# 🧹 clean.py — Automatic Downloads Organizer

`clean.py` is a Python script that monitors your **Downloads** folder in real-time and automatically organizes files into categorized folders based on their type.

## ✨ Features

- Monitors the Downloads folder continuously using the `watchdog` library
- Automatically moves files to:
  - 📁 `Downloaded Images`
  - 📁 `Downloaded Videos`
  - 📁 `Downloaded Documents`
  - 📁 `Unknown Download` (for uncategorized files)
- Supports a wide range of file formats
- Reduces clutter and improves productivity

---

## 🛠️ Requirements

- Python 3.x
- `watchdog` library

You can install the required dependency with:

```bash
pip install watchdog
