# 🕵️ MetaWraith

> **Advanced Metadata Extraction & Forensic Analysis Engine**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge\&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge\&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <img src="logo.png" width="120" alt="MetaWraith Logo">
</p>

---

## Overview

**MetaWraith** is a Python-based OSINT and digital forensics dashboard that unifies
**network metadata intelligence** and **deep file forensic analysis** into a single, cyber-themed GUI.

Built for students, security researchers, and forensic analysis workflows.

---

## Features

### Network Intelligence

* Extracts HTTP headers and server metadata
* Parses HTML meta tags (description, keywords, author, generator)
* Detects OpenGraph and Twitter Card data

### File Forensics

* GPS & hidden geolocation extraction
* Camera and device fingerprinting
* Software, edit history & document metadata
* Powered by **ExifTool** (industry standard)

### Application

* Dark-mode cyber UI (CustomTkinter)
* Multi-threaded scanning (non-blocking)
* Automatic timestamped report generation
* Executable-ready (PyInstaller compatible)

---

## How It Works

* **Web Scan:** Uses `requests` and `BeautifulSoup4` to fetch and parse metadata from target URLs.
* **File Forensics:** Executes `exiftool.exe` via `subprocess`, cleans raw output, and displays it in the dashboard.

All scan results are automatically saved to disk.

---

## Installation

### Option 1: Windows Executable

1. Visit the **Releases** page
   [https://github.com/BGx-11/MetaWraith/releases](https://github.com/BGx-11/MetaWraith/releases)
2. Download `MetaWraith.exe`
3. Run directly (no setup required)

---

### Option 2: Run from Source

```bash
git clone https://github.com/BGx-11/MetaWraith.git
cd MetaWraith
pip install -r requirements.txt
python metawraith.py
```

Ensure `exiftool.exe` exists in the project root.

---

## Usage

1. Launch **MetaWraith**
2. Choose **Network Scan** or **File Forensics**
3. Enter a URL or select a local file
4. Click **INITIATE SCAN** / **ENGAGE WRAITH**
5. View results in-app
6. Find saved reports in `wraith_dumps/`

---

## Project Structure

```text
MetaWraith/
├── exiftool_files/
├── wraith_dumps/
├── exiftool.exe
├── logo.ico
├── metawraith.py
├── requirements.txt
└── README.md
```

---

## Disclaimer

**MetaWraith is intended for educational and authorized security testing only.**
Do not scan targets or analyze files without explicit permission.

---

## License

Licensed under the **MIT License**.

---

<p align="center">
<strong>Developed by BGx (Devansh Agarwal)</strong><br>
<em>Cybersecurity Enthusiast & Developer</em>
</p>
