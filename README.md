

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

Berikut **panduan lengkap cara menggunakan tools** `pajar.py` buatan kamu:

---

### **1. Persiapan**
#### a. Install Python Modules (jika belum)
```bash
pip install requests termcolor
```

#### b. Pindah ke direktori tempat script `pajar.py`
```bash
cd ~/tools
```

---

### **2. Buat File Target**
File ini berisi daftar URL yang akan discan.
```bash
nano pwk.txt
```

**Contoh isi file:**
```
http://example.com/index.php?id=1
http://test.com/search.php?q=test
```

Simpan dengan:
- Tekan `CTRL + X`
- Ketik `Y`, lalu `Enter`

---

### **3. Jalankan Tools**
```bash
python3 pajar.py
```

---

### **4. Pilih Mode Scan**
Setelah tools jalan:
- Masukkan nama file target: `pwk.txt`
- Pilih jenis scan (contoh: `1` untuk XSS, `2` untuk SQLi, dll)
- Konfirmasi dengan `y` saat ditanya "Lanjutkan?"

---

### **5. Jenis Scan yang Tersedia**
| Nomor | Jenis Scan         |
|-------|---------------------|
| 1     | Scan XSS            |
| 2     | Scan SQL Injection  |
| 3     | Scan Redirect       |
| 4     | Scan LFI            |
| 5     | Scan HTML Injection |
| 6     | Scan .env Leak      |
| 7     | Scan Admin Panel    |
| 8     | SEMUA SCAN          |

---

### **6. Hasil**
Langkah melihat hasil:
Tampilkan isi folder sebelumnya:
pesta

Salin kode
ls
Pastikan ada berkas hasil.txtdi situ.

 Buka hasil.txt untuk dibaca:
pesta

Salin kode
nano hasil.txt
Kalau kamu cuma mau lihat tanpa edit:

pesta

Salin kode
cat hasil.txt
---

