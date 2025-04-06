

---

## **VULNERABILITY Scanner by @pajarpriandana**

### **Deskripsi Singkat:**
`pajar.py` adalah sebuah tools scanner kerentanan website yang ditulis menggunakan Python. Tools ini mampu mendeteksi berbagai celah keamanan umum seperti XSS, SQL Injection, Open Redirect, LFI, HTML Injection, .env leak, hingga admin panel exposure. Cocok digunakan oleh bug hunter, pentester, atau siapa pun yang ingin melakukan *security assessment* sederhana terhadap website.

---

### **Fitur:**

- **[1] XSS Scanner** – Mendeteksi *Cross-Site Scripting* melalui parameter URL.
- **[2] SQL Injection Scanner** – Menguji kemungkinan celah SQL Injection (Auth Bypass).
- **[3] Open Redirect Scanner** – Mengecek manipulasi redirect URL.
- **[4] LFI Scanner** – Deteksi *Local File Inclusion* yang memungkinkan akses file internal server.
- **[5] HTML Injection** – Menguji penyisipan kode HTML berbahaya di parameter.
- **[6] .env Leak Scanner** – Mengecek apakah file `.env` dapat diakses publik.
- **[7] Admin Panel Finder** – Mendeteksi path login admin yang umum digunakan.
- **[8] Scan All** – Menjalankan semua mode scan sekaligus.

---

### **Kelebihan:**

- Payload otomatis diambil dari GitHub (terbaru dan selalu update).
- Tampilan interaktif dengan warna (menggunakan `colorama`).
- Laporan disimpan ke file `hasil.txt` untuk dokumentasi hasil scan.
- Kompatibel dengan Termux dan lingkungan Linux.
- Deteksi hasil langsung: `scan > website VULN` atau `scan > no vuln`.

---

### **Cara Menggunakan:**

1. Pastikan Python 3 dan modul `requests` serta `colorama` sudah terinstal:
   ```bash
   pip install requests colorama
   ```
2. Jalankan tools:
   ```bash
   python3 pajar.py
   ```
3. Masukkan nama file target (misal `targets.txt`).
4. Pilih tipe scan yang diinginkan (pisahkan dengan koma jika lebih dari satu).
5. Tunggu hasil scan ditampilkan dan disimpan otomatis ke `hasil.txt`.

---

