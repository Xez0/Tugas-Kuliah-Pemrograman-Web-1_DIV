# DESIGN SYSTEM & VISUAL DIRECTION
## Proyek: NusantaraVenture (Travel Wisata Kepulauan Indonesia)
**Mata Kuliah:** Pemrograman Web 1 | **Variasi NIM:** 241011402572 (Hadi Sulaiman)

---

## 1. Design Read & Purpose
- **Page Kind:** Editorial Travel Journal & Booking Interface for Archipelago Expeditions
- **Audience:** Pelancong minat khusus keindahan alam Indonesia, dosen & asisten laboratorium Pemrograman Web 1
- **Visual Language:** Jurnal ekspedisi bahari nusantara: tipografi tajam berkarakter, palet warna pigmen mineral alami (basalt, terakota rempah, pasir gamping, dan biru laut dalam), garis struktural halus (hairline borders), serta ketiadaan elemen dekoratif tanpa fungsi (*no AI-slop pills, no emojis, no gratuitous glow*).
- **Dials:**
  - **ENERGY:** 2 (Balanced, berwibawa, profesional)
  - **RHYTHM:** 2 (Terstruktur rapi dengan pembeda konten yang jelas)
  - **MOTION:** 1 (Mikro-interaksi halus pada hover dan fokus keyboard, zero distraction)

---

## 2. Color Palette (Pigmen Alam Nusantara)
- `--color-ink`: `#0f1b26` (Tinta basalt lautan dalam untuk teks utama)
- `--color-canvas`: `#f8f6f2` (Kertas gamping alami bertekstur tenang)
- `--color-surface`: `#ffffff` (Permukaan kartu konten bersih)
- `--color-border`: `#e2ded7` (Garis pembagi editorial tipis)
- `--color-accent-terracotta`: `#b85435` (Aksen tembikar & rempah nusantara untuk CTA utama)
- `--color-accent-lagoon`: `#1d4e5f` (Biru laguna dalam untuk navigasi dan penanda lokasi)
- `--color-text-muted`: `#5a6773` (Teks sekunder berdaya kontras tinggi WCAG AAA)

---

## 3. Typography Hierarchy
- **Display & Judul Utama:** `Plus Jakarta Sans` (700/800) bersanding dengan aksen editorial serif `Playfair Display` (700) untuk tajuk utama yang berwibawa.
- **Teks Tubuh (Body):** `Plus Jakarta Sans` (400, 500), ukuran 13px, tinggi baris 1.6, panjang baris 65–75ch.
- **Prinsip Anti-Slop:**
  - Bebas karakter em dash (`—`). Menggunakan koma, titik dua, atau tanda kurung.
  - Bebas label eyebrow pill kapsul generik di atas heading.
  - Bebas teks gradien yang mengorbankan keterbacaan.
  - Mengganti seluruh emoji font dengan sistem ikon inline SVG bergaris 1.5px konsisten.

---

## 4. Preservasi Formula Penugasan NIM (241011402572)
- **Lebar Wrapper:** `840px` (700 + 7 × 20 px)
- **Tinggi Header:** `100px` (80 + 2 × 10 px)
- **Lebar Sidebar:** `210px` / `25%` dari area utama
- **Jarak Margin Antarkolom:** `14px` (7 × 2 px)
- **Tinggi Minimum Content:** `240px` (200 + 2 × 20 px)
- **Layout Wajib:** Header, Sidebar Kiri, Content Dua Bagian, Footer.
