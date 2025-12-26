# 🕵️ MetaWraith

> **Advanced Metadata Extraction & Digital Forensic Intelligence Engine**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge\&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <img src="logo.png" width="120" alt="MetaWraith Logo">
</p>

---

## 🧠 Overview

**MetaWraith** is a cyber-themed OSINT and digital forensics dashboard built in Python.
It combines **network intelligence** and **deep file metadata forensics** into a single, sleek GUI powered by `CustomTkinter`.

Designed for **students, security researchers, and forensic analysts**, MetaWraith extracts hidden metadata, fingerprints devices, and generates timestamped intelligence reports automatically.

---

## ✨ Key Features

### 🌐 Network Intelligence (Web Scanner)

* Extracts HTTP response headers
* Parses HTML metadata:

  * Description
  * Keywords
  * Author
  * Generator
* Detects OpenGraph & Twitter Card tags
* Auto-formats results for readability

### 📂 Deep File Forensics

* GPS & geolocation extraction from images
* Camera & device fingerprinting
* Software & editing history detection
* Document metadata analysis (PDF / DOCX)
* Powered by **ExifTool** (industry-standard forensic engine)

### 🖥️ Application Capabilities

* Dark-mode cyber UI (CustomTkinter)
* Multi-threaded scanning (no UI freezing)
* Automatic report generation
* Timestamped forensic logs
* Executable-ready (PyInstaller compatible)

---

## ⚙️ How It Works

### 🔍 Web Scan Engine

* Uses `requests` to fetch target content
* Parses HTML using `BeautifulSoup4`
* Filters and displays meaningful metadata
* Results saved automatically to disk

### 🧬 File Forensic Engine

* Interfaces directly with `exiftool.exe`
* Executes forensic commands via `subprocess`
* Cleans raw output for analyst-friendly viewing
* Logs results to secure text reports

---

## 🚀 Installation

### Option 1: Windows Executable (Recommended)

No setup required.

1. Go to **Releases**
   👉 [https://github.com/BGx-11/MetaWraith/releases](https://github.com/BGx-11/MetaWraith/releases)
2. Download `MetaWraith.exe`
3. Double-click to launch

---

### Option 2: Run from Source (Developers)

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/BGx-11/MetaWraith.git
cd MetaWraith
```

#### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Verify ExifTool

Make sure `exiftool.exe` exists in the project root.

#### 4️⃣ Run the App

```bash
python metawraith.py
```

---

## 🧪 Usage Guide

1. Launch **MetaWraith**
2. Choose a mode:

   * **NETWORK SCAN** → Website metadata
   * **FILE FORENSICS** → Local file analysis
3. Provide input:

   * URL (e.g. `https://example.com`)
   * OR select a file (image / document)
4. Click **INITIATE SCAN** or **ENGAGE WRAITH**
5. View results in the terminal panel
6. Find saved reports inside `wraith_dumps/`

---

## 📁 Project Structure

```text
MetaWraith/
├── exiftool_files/      # ExifTool support files
├── wraith_dumps/        # Auto-generated scan reports
├── exiftool.exe         # Forensic engine
├── logo.ico             # App icon
├── logo.png             # README / UI logo
├── metawraith.py        # Main application
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## ⚠️ Requirements

* Python **3.10+**
* Windows OS
* Internet connection (for web scans)

### Python Libraries

* `customtkinter`
* `requests`
* `beautifulsoup4`

(All listed in `requirements.txt`)

---

## 🔐 Ethical Disclaimer

> **MetaWraith is intended strictly for educational and authorized security testing.**

* Do **NOT** scan websites without permission
* Do **NOT** analyze files you do not own or have consent for
* The developer is **not responsible** for misuse or legal consequences

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it with proper credit.

---

## 👨‍💻 Author

**Devansh Agarwal (BGx)**
Security Researcher • Student • Builder

🔗 GitHub: [https://github.com/BGx-11](https://github.com/BGx-11)
