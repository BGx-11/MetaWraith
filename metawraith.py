import customtkinter as ctk
from tkinter import filedialog
import os
import sys
import datetime
import subprocess
import requests
from bs4 import BeautifulSoup
import threading

# --- THEME CONFIGURATION ---
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")  # Base theme

# Colors
COLOR_BG = "#1a1a1a"       # Dark Gray Background
COLOR_ACCENT = "#1f6aa5"   # Blue Accent (Wraith Blue)
COLOR_TEXT = "#e1e1e1"     # Off-white text
COLOR_TERMINAL = "#0c0c0c"# Deep black for console
COLOR_GREEN = "#2CC985"    # Success Green
COLOR_RED = "#E04F5F"      # Error Red

# --- SYSTEM PATHS ---
SAVE_FOLDER = "wraith_dumps"

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

if os.name == 'nt':
    ENGINE_PATH = resource_path("exiftool.exe")
else:
    ENGINE_PATH = resource_path("exiftool")

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

# --- MAIN APPLICATION ---
class MetaWraithApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Config
        self.title("MetaWraith v1.0")
        self.geometry("1000x700")
        self.minsize(800, 600)

        # --- SET WINDOW ICON ---
        try:
            # Use resource_path so it finds the icon even after compiling
            icon_path = resource_path("logo.ico")
            self.iconbitmap(icon_path)
        except Exception:
            # Fail silently if logo.ico is missing, app will still run
            pass
        
        # Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#111111")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)

        # Logo / Title
        self.logo_lbl = ctk.CTkLabel(self.sidebar, text="META\nWRAITH", 
                                     font=ctk.CTkFont(family="Roboto Medium", size=26, weight="bold"),
                                     text_color=COLOR_TEXT)
        self.logo_lbl.grid(row=0, column=0, padx=20, pady=(30, 20))

        # Sidebar Buttons
        self.info_lbl = ctk.CTkLabel(self.sidebar, text="SYSTEM READY", text_color=COLOR_GREEN, font=("Consolas", 12))
        self.info_lbl.grid(row=1, column=0, padx=20, pady=10)

        # Version Footer
        self.ver_lbl = ctk.CTkLabel(self.sidebar, text="Build 2025.12\nDevansh Agarwal (BGx)", text_color="gray40")
        self.ver_lbl.grid(row=5, column=0, padx=20, pady=20)

        # --- MAIN CONTENT AREA ---
        self.main_panel = ctk.CTkFrame(self, corner_radius=0, fg_color=COLOR_BG)
        self.main_panel.grid(row=0, column=1, sticky="nsew")
        self.main_panel.grid_rowconfigure(1, weight=1)
        self.main_panel.grid_columnconfigure(0, weight=1)

        # Header
        self.header = ctk.CTkLabel(self.main_panel, text=" // INTELLIGENCE DASHBOARD", 
                                   font=("Consolas", 16), text_color="gray60", anchor="w")
        self.header.grid(row=0, column=0, padx=30, pady=(20, 10), sticky="ew")

        # Tabs System
        self.tabs = ctk.CTkTabview(self.main_panel, width=750, height=500, 
                                   fg_color="#222222", text_color=COLOR_TEXT)
        self.tabs.grid(row=1, column=0, padx=30, pady=10, sticky="nsew")
        
        # Create Tabs
        self.tab_web = self.tabs.add("  NETWORK SCAN  ")
        self.tab_file = self.tabs.add("  FILE FORENSICS  ")

        # Setup Tab UIs
        self.setup_web_ui()
        self.setup_file_ui()

        # --- STATUS BAR ---
        self.status_bar = ctk.CTkLabel(self.main_panel, text="Idle...", height=30, 
                                       fg_color="#0f0f0f", text_color="gray", anchor="w")
        self.status_bar.grid(row=2, column=0, sticky="ew", padx=0, pady=0)
        self.status_bar.configure(padx=10)

    # --- UI: WEB SCANNER ---
    def setup_web_ui(self):
        self.tab_web.grid_columnconfigure(0, weight=1)
        self.tab_web.grid_rowconfigure(2, weight=1)

        input_frame = ctk.CTkFrame(self.tab_web, fg_color="transparent")
        input_frame.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        self.url_entry = ctk.CTkEntry(input_frame, placeholder_text="Enter Target URL (e.g. https://site.com)", height=45)
        self.url_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        scan_btn = ctk.CTkButton(input_frame, text="INITIATE SCAN", width=140, height=45, 
                                 fg_color=COLOR_ACCENT, hover_color="#144d7a",
                                 font=("Roboto", 12, "bold"), command=self.start_web_thread)
        scan_btn.pack(side="right")

        self.web_out = ctk.CTkTextbox(self.tab_web, fg_color=COLOR_TERMINAL, text_color=COLOR_GREEN, 
                                      font=("Consolas", 13), activate_scrollbars=True)
        self.web_out.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # --- UI: FILE FORENSICS ---
    def setup_file_ui(self):
        self.tab_file.grid_columnconfigure(0, weight=1)
        self.tab_file.grid_rowconfigure(2, weight=1)

        input_frame = ctk.CTkFrame(self.tab_file, fg_color="transparent")
        input_frame.grid(row=0, column=0, padx=10, pady=15, sticky="ew")

        self.file_path_entry = ctk.CTkEntry(input_frame, placeholder_text="Select Target Artifact...", height=45)
        self.file_path_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        browse_btn = ctk.CTkButton(input_frame, text="BROWSE", width=100, height=45, 
                                   fg_color="#444444", hover_color="#333333", command=self.browse_file)
        browse_btn.pack(side="left", padx=(0, 10))

        analyze_btn = ctk.CTkButton(input_frame, text="ENGAGE WRAITH", width=140, height=45, 
                                    fg_color="#C92C3A", hover_color="#8a1c26",
                                    font=("Roboto", 12, "bold"), command=self.start_file_thread)
        analyze_btn.pack(side="right")

        self.file_out = ctk.CTkTextbox(self.tab_file, fg_color=COLOR_TERMINAL, text_color=COLOR_GREEN, 
                                       font=("Consolas", 13), activate_scrollbars=True)
        self.file_out.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    # --- FUNCTIONS ---
    def set_status(self, text, is_error=False):
        color = COLOR_RED if is_error else "gray"
        self.status_bar.configure(text=f"> SYSTEM: {text}", text_color=color)

    def browse_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.file_path_entry.delete(0, "end")
            self.file_path_entry.insert(0, path)

    # --- THREADING & LOGIC ---
    def start_web_thread(self):
        url = self.url_entry.get()
        if not url: return
        self.web_out.delete("1.0", "end")
        self.web_out.insert("end", "[*] Initializing Network Probe...\n")
        self.set_status("Scanning URL...")
        threading.Thread(target=self.run_web_scan, args=(url,), daemon=True).start()

    def start_file_thread(self):
        path = self.file_path_entry.get().replace('"', '')
        if not path: return
        self.file_out.delete("1.0", "end")
        self.file_out.insert("end", "[*] Initializing Forensic Engine...\n")
        self.set_status("Analyzing File Artifact...")
        threading.Thread(target=self.run_file_scan, args=(path,), daemon=True).start()

    # --- ENGINES ---
    def run_web_scan(self, url):
        try:
            if not url.startswith(('http://', 'https://')):
                url = 'http://' + url
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            data = []
            data.append(f"TARGET: {url}")
            data.append(f"STATUS: {response.status_code}")
            data.append("-" * 40)
            data.append(f"TITLE : {soup.title.string.strip() if soup.title else 'N/A'}")
            for tag in soup.find_all('meta'):
                name = tag.get('name') or tag.get('property')
                content = tag.get('content')
                if name and content:
                    data.append(f"{name.upper().ljust(15)} : {content}")

            result_text = "\n".join(data)
            self.update_ui(self.web_out, result_text, "website")

        except Exception as e:
            self.update_ui(self.web_out, f"[!] CONNECTION FAILED: {e}", None, True)

    def run_file_scan(self, filepath):
        if not os.path.exists(filepath):
            self.update_ui(self.file_out, "[!] ERROR: Artifact not found.", None, True)
            return
        if not os.path.exists(ENGINE_PATH):
            self.update_ui(self.file_out, f"[!] FATAL: Forensic Engine (core) missing.\nPlease reinstall or check directory.", None, True)
            return
        try:
            process = subprocess.run(
                [ENGINE_PATH, "-a", "-u", "-g1", "-s", filepath],
                capture_output=True, text=True, encoding='utf-8', errors='ignore'
            )
            clean_lines = []
            skip = False
            for line in process.stdout.splitlines():
                if "---- ExifTool ----" in line: skip = True; continue
                if skip and line.startswith("---- "): skip = False
                if not skip: clean_lines.append(line)

            result_text = "\n".join(clean_lines)
            if not result_text.strip():
                result_text = "[*] No hidden metadata found on this artifact."

            self.update_ui(self.file_out, result_text, os.path.basename(filepath))

        except Exception as e:
            self.update_ui(self.file_out, f"[!] SYSTEM FAILURE: {e}", None, True)

    def update_ui(self, widget, content, source_name=None, is_error=False):
        self.after(0, lambda: self._finalize_ui(widget, content, source_name, is_error))

    def _finalize_ui(self, widget, content, source_name, is_error):
        widget.delete("1.0", "end")
        widget.insert("end", content)
        if is_error:
            self.set_status("Operation Failed", True)
        else:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            safe_name = "".join([c for c in source_name if c.isalnum() or c in (' ', '-', '_')]).strip()[:15]
            filename = f"{SAVE_FOLDER}/{safe_name}_{timestamp}.txt"
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write("METAWRAITH INTELLIGENCE REPORT\n")
                    f.write(f"Target: {source_name}\n")
                    f.write(f"Timestamp: {timestamp}\n")
                    f.write("="*40 + "\n\n")
                    f.write(content)
                widget.insert("end", f"\n\n[+] REPORT SECURED: {filename}")
                self.set_status(f"Scan Complete. Data saved to {filename}")
            except:
                widget.insert("end", "\n\n[!] WARNING: Could not save log file.")
                self.set_status("Scan Complete (Save Failed)", True)

if __name__ == "__main__":
    app = MetaWraithApp()
    app.mainloop()