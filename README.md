# Tugas Pemrograman Web 1: Merancang Layout Website Menggunakan DIV dan CSS Berdasarkan Variasi NIM

Proyek penugasan mata kuliah **Pemrograman Web 1** pada Program Studi Teknik Informatika S-1, Fakultas Ilmu Komputer, Universitas Pamulang.

---

## Identitas Mahasiswa
- **Nama Mahasiswa :** Hadi Sulaiman
- **NIM :** 241011402572
- **Kelas :** 05TPLM003
- **Program Studi :** Teknik Informatika S-1
- **Fakultas :** Ilmu Komputer
- **Perguruan Tinggi :** Universitas Pamulang
- **Mata Kuliah :** Pemrograman Web 1
- **Topik Penugasan :** Merancang Layout Website Menggunakan `<div>` dan CSS Berdasarkan Variasi NIM

---

## Petunjuk Penugasan
Website dirancang menggunakan HTML dan CSS murni dengan memanfaatkan tag `<div>` sebagai pembentuk struktur halaman. Halaman wajib memiliki bagian **Header, Sidebar, Content, dan Footer**, serta menerapkan aturan kalkulasi CSS berdasarkan variasi NIM mahasiswa.

![Petunjuk Tugas](images/petunjuk_tugas.jpg)

---

## 1. Penentuan Tema & Layout Wajib Berdasarkan Digit Terakhir NIM
Digit terakhir dari NIM **241011402572** adalah angka **`2`**.

| Digit | Tema Website | Layout Wajib | Status Pemilihan |
| :---: | :--- | :--- | :---: |
| 0 | Portal Kampus | Header, sidebar kiri, content, footer | - |
| 1 | Coffee Shop | Header, content, sidebar kanan, footer | - |
| **2** | **Travel Wisata** | **Header, sidebar kiri, content dua bagian, footer** | **TERPILIH (&check;)** |
| 3 | Gaming Center | Header, dua sidebar, content tengah, footer | - |
| 4 | Hotel | Header, menu atas, content, sidebar kanan, footer | - |
| 5 | Fashion Store | Header, sidebar kiri, content tiga bagian, footer | - |
| 6 | Perpustakaan Digital | Header, sidebar kiri, content, footer | - |
| 7 | Event dan Seminar | Header, menu atas, content dua bagian, footer | - |
| 8 | Computer Store | Header, sidebar kiri, content, panel kanan, footer | - |
| 9 | Restaurant | Header, menu atas, content dua bagian, footer | - |

---

## 2. Perhitungan Formula CSS Berdasarkan 5 Digit Terakhir NIM
NIM: **`2 4 1 0 1 1 4 0 2 5 7 2`**  
Lima digit terakhir dari kiri ke kanan: **`0, 2, 5, 7, 2`**  
*Aturan Khusus Penugasan:* *"Jika terdapat digit 0, ganti menjadi 7 dalam perhitungan berikut."*

| Posisi Digit | Digit Asli | Digit Dihitung | Ketentuan / Rumus CSS | Perhitungan Matematis | Nilai Implementasi CSS | Selector CSS Terkait |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- |
| **Digit ke-1** | `0` | **`7`** *(diubah dari 0)* | Lebar wrapper = $700 + (\text{digit} \times 20)\text{ px}$ | $700 + (7 \times 20) = 700 + 140$ | **`840px`** | `#wrapper`, `.wrapper` |
| **Digit ke-2** | `2` | **`2`** | Tinggi header = $80 + (\text{digit} \times 10)\text{ px}$ | $80 + (2 \times 10) = 80 + 20$ | **`100px`** | `#header`, `.header` |
| **Digit ke-3** | `5` | **`5`** | Lebar sidebar utama = $15 + (\text{digit} \times 2)\%$ dari lebar area utama | $15 + (5 \times 2)\% = 15 + 10\%$ | **`25%` (`210px`)** | `#sidebar`, `.sidebar` |
| **Digit ke-4** | `7` | **`7`** | Jarak margin antarkolom = $\text{digit} \times 2\text{ px}$ | $7 \times 2$ | **`14px`** | `.sidebar { margin-right: 14px; }`<br>`.content-col.col-left { margin-right: 14px; }` |
| **Digit ke-5** | `2` | **`2`** | Tinggi minimum content = $200 + (\text{digit} \times 20)\text{ px}$ | $200 + (2 \times 20) = 200 + 40$ | **`240px`** | `#content`, `.content-area`, `.content-col` |

---

## 3. Verifikasi Geometri & Presisi Tata Letak (Box Model)
Semua ukuran kolom telah diverifikasi dengan presisi piksel:
$$\begin{aligned}
\text{Lebar Area Utama} &= 840\text{ px} \\
\text{Lebar Sidebar Kiri} &= 200\text{ px (25\% area dalam)} \\
\text{Margin Antarkolom} &= 14\text{ px} \\
\text{Lebar Area Content} &= 840\text{ px} - (14\text{ px} \times 2\text{ padding}) - 200\text{ px} - 14\text{ px} = 598\text{ px} \\
\text{Lebar Kolom 1 (Kiri)} &= \frac{598\text{ px} - 14\text{ px}}{2} = 292\text{ px} \\
\text{Margin Antar Bagian Content} &= 14\text{ px} \\
\text{Lebar Kolom 2 (Kanan)} &= 292\text{ px} \\
\text{Total Lebar Bagian Content} &= 292\text{ px} + 14\text{ px} + 292\text{ px} = 598\text{ px} \quad (\text{Presisi 100\%})
\end{aligned}$$

---

## 4. Struktur Berkas Proyek

```
Tugas-Kuliah-Pemrograman-Web-1_DIV/
├── index.html                  # Halaman Beranda Utama (Header, Sidebar Kiri, Content 2 Bagian, Footer)
├── destinasi.html              # Halaman Katalog Wisata (Layout DIV Konsisten, Dua Kolom Destinasi)
├── kontak.html                 # Halaman Kontak & Reservasi (Formulir Pemesanan & Info Kantor)
├── style.css                   # Berkas Eksternal CSS Tata Letak DIV & Aturan Formula NIM
├── images/                     # Direktori Aset Media & Fotografi Wisata
│   ├── petunjuk_tugas.jpg      # Foto Panduan Soal Penugasan Dosen
│   ├── hero-marine.jpg         # Gambar Hero Header Wisata
│   ├── raja-ampat.jpg          # Destinasi Raja Ampat, Papua
│   ├── bromo.jpg               # Destinasi Gunung Bromo, Jawa Timur
│   ├── labuan-bajo.jpg         # Destinasi Labuan Bajo & Komodo, NTT
│   ├── nusa-penida.jpg         # Destinasi Nusa Penida, Bali
│   ├── kawah-ijen.jpg          # Destinasi Kawah Ijen Blue Fire, Jawa Timur
│   ├── cappadocia.jpg          # Aset Tambahan
│   └── kyoto.jpg               # Aset Tambahan
├── screenshot_index.png        # Tangkapan Layar Tampilan Asli Halaman Beranda
├── screenshot_destinasi.png    # Tangkapan Layar Tampilan Asli Halaman Destinasi
├── screenshot_kontak.png       # Tangkapan Layar Tampilan Asli Halaman Kontak
├── .gitignore                  # Berkas Pengabaian Git
└── README.md                   # Dokumentasi Teknis Komprehensif
```

---

## 5. Fitur Halaman Website

### A. Halaman Beranda (`index.html`)
- **Header:** Tinggi 100px, warna gradien maritim modern, logo pesawat terbang, nama brand **NusantaraVenture**, dan lencana identitas NIM mahasiswa.
- **Sidebar Kiri:** Lebar proporsional 25%, berisi menu navigasi halaman, widget identitas mahasiswa (Hadi Sulaiman - 241011402572), promo eksklusif diskon 30%, serta info layanan pelanggan.
- **Content Area (Dua Bagian):**
  - **Bagian 1 (Kolom Kiri):** Destinasi Unggulan (Raja Ampat & Gunung Bromo) lengkap dengan kartu foto, tag kategori, deskripsi, harga, dan tombol detail.
  - **Bagian 2 (Kolom Kanan):** Paket Tour Populer (Labuan Bajo Phinisi & Nusa Penida Island) dengan informasi jadwal dan harga paket.
- **Tabel Verifikasi NIM:** Menampilkan tabel rincian formula perhitungan CSS yang tertanam langsung di halaman web.
- **Footer:** Menutup layout dengan 3 kolom informatif (Tentang Kami, Navigasi Halaman, Info Akademik) dan teks hak cipta.

### B. Halaman Katalog Destinasi (`destinasi.html`)
- Mempertahankan konsistensi tata letak `<div>` dan aturan formula CSS NIM.
- Menampilkan filter kategori wisata (Wisata Bahari, Pegunungan, Budaya, Kuliner).
- Konten dua bagian menyajikan kartu destinasi wisata bahari dan pegunungan dengan tombol aksi reservasi.

### C. Halaman Kontak & Reservasi (`kontak.html`)
- Mempertahankan struktur tata letak `<div>` dan CSS formula NIM.
- Konten bagian kiri menyajikan formulir interaktif (Nama, Email, WhatsApp, Pilihan Destinasi, Pesan Khusus).
- Konten bagian kanan memuat data alamat kantor operasional, kontak telepon, jam operasional, dan garansi layanan 100%.

---

## 6. Pratinjau Tangkapan Layar

### Tampilan Halaman Utama (`index.html`)
![Screenshot Index](screenshot_index.png)

### Tampilan Halaman Destinasi (`destinasi.html`)
![Screenshot Destinasi](screenshot_destinasi.png)

### Tampilan Halaman Kontak (`kontak.html`)
![Screenshot Kontak](screenshot_kontak.png)

---

## 7. Cara Menjalankan Proyek
1. Clone repositori ini melalui terminal:
   ```bash
   git clone https://github.com/Xez0/Tugas-Kuliah-Pemrograman-Web-1_DIV.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd Tugas-Kuliah-Pemrograman-Web-1_DIV
   ```
3. Buka berkas `index.html` langsung pada peramban web modern Anda (Google Chrome, Microsoft Edge, Mozilla Firefox, Safari, dll).
