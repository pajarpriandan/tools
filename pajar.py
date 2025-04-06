import requests
import sys
import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from colorama import Fore, Style, init
init(autoreset=True)

requests.packages.urllib3.disable_warnings()

# ASCII banner
print(Fore.RED + r"""
     ██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███╗   ██╗
     ██║   ██║██║   ██║██║     ████╗  ██║████╗  ██║
     ██║   ██║██║   ██║██║     ██╔██╗ ██║██╔██╗ ██║
     ╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║██║╚██╗██║
      ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║██║ ╚████║
       ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═══╝
""" + Fore.CYAN + """
VULNERABILITY Scanner by @pajarpriandana
Follow IG: @ox_pajarpriandana
""")

# Loading efek
print(Fore.YELLOW + "[*] Loading modules", end="")
for _ in range(5):
    print(".", end="", flush=True)
    time.sleep(0.3)
print("\n")

# Input file
filename = input(Fore.CYAN + "[?] Masukkan nama file target (contoh: targets.txt): ").strip()

# Menu scan
menu = {
    "1": "xss",
    "2": "sqli",
    "3": "open_redirect",
    "4": "lfi",
    "5": "html_injection",
    "6": "env",
    "7": "admin_panel",
    "8": "all"
}

print(Fore.GREEN + "\n[ PILIH TIPE SCAN ]")
print(" 1) Scan XSS")
print(" 2) Scan SQLi")
print(" 3) Scan Redirect")
print(" 4) Scan LFI")
print(" 5) Scan HTML Injection")
print(" 6) Scan .env Leak")
print(" 7) Scan Admin Panel")
print(" 8) SEMUA SCAN")

while True:
    choice_input = input(Fore.CYAN + "\n[?] Pilihan kamu (contoh: 1,2,4): ").strip()
    choices = [x.strip() for x in choice_input.split(",") if x.strip() in menu]
    if choices:
        break
    print(Fore.RED + "[!] Pilihan tidak valid. Gunakan angka 1-8, pisahkan dengan koma.")

scan_modes = [menu[c] for c in choices]
print(Fore.MAGENTA + f"\n[!] Akan scan dengan mode: {', '.join(scan_modes).upper()}")
confirm = input(Fore.CYAN + "[?] Lanjutkan? (y/n): ").lower()
if confirm != "y":
    print(Fore.YELLOW + "[*] Dibatalkan oleh user.")
    sys.exit()

# Payload sources
payload_sources = {
    "xss": "https://raw.githubusercontent.com/payloadbox/xss-payload-list/master/Intruder/xss-payload-list.txt",
    "sqli": "https://raw.githubusercontent.com/payloadbox/sql-injection-payload-list/master/Intruder/exploit/Auth_Bypass.txt",
    "open_redirect": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Open%20Redirect/Intruder/Open-Redirect-payloads.txt",
    "lfi": "https://raw.githubusercontent.com/emadshanab/LFI-Payload-List/master/LFI%20payloads.txt",
    "html_injection": "https://raw.githubusercontent.com/InfoSecWarrior/Offensive-Payloads/main/Html-Injection-Payloads.txt",
    "env": "https://raw.githubusercontent.com/coffinxp/payloads/main/env.txt"
}

admin_paths = [
    "/admin", "/admin/login", "/administrator", "/admin.php",
    "/admin/login.php", "/wp-admin", "/cpanel"
]

def load_payloads(selected):
    payloads = {}
    for ptype in selected:
        if ptype in payload_sources:
            try:
                print(Fore.YELLOW + f"[+] Mengambil payload {ptype} dari GitHub...")
                res = requests.get(payload_sources[ptype], timeout=10)
                payloads[ptype] = [line.strip() for line in res.text.splitlines() if line.strip() and not line.startswith("#")]
            except:
                print(Fore.RED + f"[!] Gagal mengambil payload untuk {ptype}")
                payloads[ptype] = []
    return payloads

def log_vuln(vuln_type, url):
    print(Fore.RED + f"scan > {url} VULN")
    with open("hasil.txt", "a") as f:
        f.write(f"[{vuln_type.upper()}] {url}\n")

def log_not_vuln(url):
    print(Fore.GREEN + f"vuln > {url} no vuln")

def test_payloads(url, payload_list, vuln_type):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if not query:
        return
    vuln_found = False
    for param in query:
        for payload in payload_list:
            test_query = query.copy()
            test_query[param] = payload
            full_url = urlunparse(parsed._replace(query=urlencode(test_query, doseq=True)))
            try:
                r = requests.get(full_url, timeout=10, verify=False)
                body = r.text.lower()
                if vuln_type == "xss" and payload.lower() in body:
                    log_vuln("xss", full_url)
                    vuln_found = True
                elif vuln_type == "sqli" and any(x in body for x in ["sql", "syntax", "mysql", "error"]):
                    log_vuln("sqli", full_url)
                    vuln_found = True
                elif vuln_type == "open_redirect" and r.url != full_url:
                    log_vuln("open_redirect", full_url + f" → {r.url}")
                    vuln_found = True
                elif vuln_type == "lfi" and ("root:" in body or "/bin/bash" in body):
                    log_vuln("lfi", full_url)
                    vuln_found = True
                elif vuln_type == "env" and any(x in body for x in ["apikey", "secret", "token"]):
                    log_vuln("env", full_url)
                    vuln_found = True
                elif vuln_type == "html_injection" and payload.lower() in body:
                    log_vuln("html_injection", full_url)
                    vuln_found = True
            except:
                continue
    if not vuln_found:
        log_not_vuln(url)

def test_admin_panels(domain):
    found = False
    for path in admin_paths:
        url = domain.rstrip("/") + path
        try:
            r = requests.get(url, timeout=10, verify=False)
            if r.status_code == 200 and any(x in r.text.lower() for x in ["login", "admin"]):
                log_vuln("admin_panel", url)
                found = True
        except:
            continue
    if not found:
        log_not_vuln(domain)

def main(filename, selected_modes):
    try:
        with open(filename, "r") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "[!] File tidak ditemukan.")
        return

    payloads = load_payloads(selected_modes if "all" not in selected_modes else payload_sources.keys())
    print(f"\n[*] Mulai scanning {len(urls)} target...\n")
    for url in urls:
        print(Fore.BLUE + f"[>] Scan: {url}")
        if "all" in selected_modes:
            for ptype in payloads:
                test_payloads(url, payloads[ptype], ptype)
            test_admin_panels(url.split("?")[0])
        else:
            for ptype in selected_modes:
                if ptype == "admin_panel":
                    test_admin_panels(url.split("?")[0])
                elif ptype in payloads:
                    test_payloads(url, payloads[ptype], ptype)

main(filename, scan_modes)
