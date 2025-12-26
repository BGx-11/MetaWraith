# 🕵️ MetaWraith

> **Advanced Metadata Extraction & Forensic Analysis Engine**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<br>

<p align="center">
  <img src="logo.ico" width="120" alt="MetaWraith Logo">
</p>

## Features

MetaWraith is designed to be a unified dashboard for OSINT and digital forensics.

* **🌐 Network Intelligence (Web Scanner)**
    * Extracts server headers, content types, and security configurations.
    * Scrapes meta tags (Description, Keywords, Author, Generators).
    * Identifies OpenGraph and Twitter Card data.
    
* **📂 Deep File Forensics**
    * **GPS Extraction:** Locates hidden geolocation data in images.
    * **Device Fingerprinting:** Identifies camera models, software versions, and lens serial numbers.
    * **Document Analysis:** Extracts author names, edit times, and revision history from PDF/DOCX files.
    * **Powered by ExifTool:** Uses the industry-standard Phil Harvey ExifTool engine.

* **🖥️ Application Features**
    * **Dark Mode UI:** Professional cyber-themed interface built with CustomTkinter.
    * **Auto-Reporting:** Automatically saves every scan result to a timestamped text file in `wraith_dumps/`.
    * **Multi-threading:** Ensures smooth performance during heavy scan operations.

## How It Works

MetaWraith operates as a GUI wrapper around powerful backend engines:

1.  **Web Scan:** Uses `requests` and `BeautifulSoup4` to establish a connection to the target URL, parse the HTML structure, and filter out relevant metadata tags and HTTP headers.
2.  **File Forensics:** Interacts with a bundled `exiftool.exe` binary. It sends command-line arguments to the engine to analyze specific files and pipes the raw output back to the MetaWraith dashboard, cleaning it for readability.

## Installation

### Option 1: For Users (Windows Executable)
No coding or installation required.
1.  Go to the [**Releases Page**](https://github.com/BGx-11/MetaWraith/releases).
2.  Download the latest `MetaWraith.exe`.
3.  Double-click to run.

### Option 2: For Developers (Source Code)
1.  Clone the repository:
    ```bash
    git clone [https://github.com/BGx-11/MetaWraith.git](https://github.com/BGx-11/MetaWraith.git)
    cd MetaWraith
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Ensure `exiftool.exe` is in the main directory (included in repo).
4.  Run the application:
    ```bash
    python metawraith.py
    ```

## Usage

1.  **Launch MetaWraith.**
2.  **Select a Mode:**
    * Click the **Network Scan** tab for websites.
    * Click the **File Forensics** tab for local files.
3.  **Input Target:**
    * **Web:** Enter a URL (e.g., `https://example.com`).
    * **File:** Click "Browse" to select an image or document.
4.  **Engage:** Click **INITIATE SCAN** or **ENGAGE WRAITH**.
5.  **View Results:** Data will appear in the terminal window.
6.  **Check Logs:** A text file report is automatically saved in the `wraith_dumps` folder.

## Project Structure

```text
MetaWraith/
├── exiftool_files/      # Support files for the forensic engine
├── wraith_dumps/        # Output folder for saved reports (Auto-generated)
├── exiftool.exe         # Core forensic engine binary
├── logo.ico             # Application icon
├── metawraith.py        # Main source code
├── requirements.txt     # Python dependencies
└── README.md            # Documentation

```

## Configuration

* **Dependencies:** The tool relies on `customtkinter`, `requests`, and `beautifulsoup4`. These are listed in `requirements.txt`.
* **ExifTool:** The tool expects `exiftool.exe` to be present in the root directory or bundled within the PyInstaller `_MEIPASS` path. If the engine is missing, the tool will alert you via the status bar.

## Disclaimer

**MetaWraith is intended for educational and authorized security testing purposes only.**
The creator (**BGx**) takes no responsibility for the misuse of this tool. Ensure you have explicit permission before scanning websites or analyzing files that do not belong to you.

## License

This project is licensed under the **MIT License**. You are free to modify, distribute, and use this code for personal or commercial projects, provided the original author is credited.

---

**Developed by [BGx**](https://www.google.com/search?q=https://github.com/BGx-11)

```

```
