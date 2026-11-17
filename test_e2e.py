"""
Suite Pengujian End-to-End (E2E) Kepatuhan Desain Anti-Slop & Formula NIM 241011402572
Penugasan: Pemrograman Web 1 (DIV & CSS) - NusantaraVenture
"""

import os
import sys
from playwright.sync_api import sync_playwright

def run_e2e():
    print("======================================================================")
    print(" MENJALANKAN SUITE PENGUJIAN END-TO-END (E2E) ARCHIPELAGO EXPEDITION")
    print(" Mahasiswa: Hadi Sulaiman | NIM: 241011402572 | Kelas: 05TPLM003")
    print(" Standar Kualitas: /frontend-design, /antislop, /impeccable")
    print("======================================================================")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_url = "file:///" + os.path.join(base_dir, "index.html").replace("\\", "/")
    destinasi_url = "file:///" + os.path.join(base_dir, "destinasi.html").replace("\\", "/")
    paket_url = "file:///" + os.path.join(base_dir, "paket.html").replace("\\", "/")
    kontak_url = "file:///" + os.path.join(base_dir, "kontak.html").replace("\\", "/")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        page = browser.new_page(viewport={"width": 1200, "height": 1400})
        
        # -------------------------------------------------------------
        # UJI 1: VERIFIKASI EKSAK FORMULA NIM DI SELURUH 4 HALAMAN
        # -------------------------------------------------------------
        print("\n[UJI 1] Verifikasi Formula Geometri NIM Eksak di Seluruh Halaman...")
        for name, url in [
            ("index.html", index_url),
            ("destinasi.html", destinasi_url),
            ("paket.html", paket_url),
            ("kontak.html", kontak_url),
        ]:
            page.goto(url)
            w_box = page.locator("#wrapper").bounding_box()
            h_box = page.locator("#header").bounding_box()
            s_box = page.locator("#sidebar").bounding_box()
            c_box = page.locator("#content").bounding_box()
            b1 = page.locator("#content-kolom-1").bounding_box()
            b2 = page.locator("#content-kolom-2").bounding_box()
            f_box = page.locator("#footer").bounding_box()

            col_gap = c_box["x"] - (s_box["x"] + s_box["width"])
            inner_gap = b2["x"] - (b1["x"] + b1["width"])
            min_h = page.locator("#content").evaluate("el => getComputedStyle(el).minHeight")
            col_min_h = page.locator("#content-kolom-1").evaluate("el => getComputedStyle(el).minHeight")
            tags = page.evaluate("() => ['#wrapper','#header','#sidebar','#content','#content-kolom-1','#content-kolom-2','#footer'].map(s => document.querySelector(s).tagName)")

            assert abs(w_box["width"] - 840) < 1, f"{name}: lebar wrapper {w_box['width']} != 840"
            assert abs(h_box["height"] - 100) < 1, f"{name}: tinggi header {h_box['height']} != 100"
            assert abs(s_box["width"] - 210) < 1, f"{name}: lebar sidebar {s_box['width']} != 210 (25% dari 840)"
            assert abs(col_gap - 14) < 1, f"{name}: margin antarkolom {col_gap} != 14"
            assert abs(inner_gap - 14) < 1, f"{name}: margin 2 bagian content {inner_gap} != 14"
            assert abs(b1["width"] - b2["width"]) < 1, f"{name}: dua bagian content tidak simetris ({b1['width']} vs {b2['width']})"
            assert min_h == "240px" and col_min_h == "240px", f"{name}: min-height bukan 240px ({min_h}, {col_min_h})"
            assert c_box["height"] >= 240, f"{name}: tinggi content {c_box['height']} < 240"
            assert s_box["x"] < c_box["x"], f"{name}: sidebar bukan di kiri content"
            assert f_box["y"] >= max(s_box["y"] + s_box["height"], c_box["y"] + c_box["height"]) - 1, f"{name}: footer overlap"
            assert all(t == "DIV" for t in tags), f"{name}: ada struktur non-DIV {tags}"
            assert page.locator("link[rel='icon']").count() == 1, f"{name}: favicon belum tertaut"
            print(f"  OK [{name}]: wrapper=840px, header=100px, sidebar=210px (25%), gap=14px, content={c_box['height']:.1f}px (>=240px)")

        # -------------------------------------------------------------
        # UJI 2: NAVIGASI LENGKAP SEMUA HALAMAN (E2E FLOW)
        # -------------------------------------------------------------
        print("\n[UJI 2] Verifikasi Alur Navigasi Antar Halaman...")
        
        # Klik link Katalog Destinasi dari Index
        page.locator("a[href='destinasi.html']").first.click()
        page.wait_for_load_state("load")
        assert "destinasi.html" in page.url
        print("  OK: Navigasi Index -> Destinasi Sukses")
        
        # Klik link Paket Layanan dari Destinasi
        page.locator("a[href='paket.html']").first.click()
        page.wait_for_load_state("load")
        assert "paket.html" in page.url
        print("  OK: Navigasi Destinasi -> Paket Layanan Sukses")
        
        # Klik link Kontak & Reservasi dari Paket
        page.locator("a[href='kontak.html']").first.click()
        page.wait_for_load_state("load")
        assert "kontak.html" in page.url
        print("  OK: Navigasi Paket Layanan -> Kontak Sukses")
        
        # Klik link Beranda Ekspedisi dari Kontak
        page.locator("a[href='index.html']").first.click()
        page.wait_for_load_state("load")
        assert "index.html" in page.url
        print("  OK: Navigasi Kontak -> Index Sukses")

        # -------------------------------------------------------------
        # UJI 3: FILTER INTERAKTIF PADA DESTINASI.HTML
        # -------------------------------------------------------------
        print("\n[UJI 3] Verifikasi Fungsi Filter Interaktif Destinasi...")
        page.goto(destinasi_url)
        
        # Filter: Bahari & Karang
        page.locator("button:has-text('Bahari & Karang')").click()
        bahari_items = page.locator(".item-bahari")
        gunung_items = page.locator(".item-gunung")
        assert bahari_items.first.is_visible(), "Item bahari harus terlihat"
        assert not gunung_items.first.is_visible(), "Item gunung harus disembunyikan"
        print("  OK: Filter 'Bahari & Karang' berhasil menyaring item vulkanik")
        
        # Filter: Vulkanik & Kaldera
        page.locator("button:has-text('Vulkanik & Kaldera')").click()
        assert not bahari_items.first.is_visible(), "Item bahari harus disembunyikan"
        assert gunung_items.first.is_visible(), "Item gunung harus terlihat"
        print("  OK: Filter 'Vulkanik & Kaldera' berhasil menyaring item bahari")
        
        # Filter: Semua Zona
        page.locator("button:has-text('Semua Zona')").click()
        assert bahari_items.first.is_visible() and gunung_items.first.is_visible()
        print("  OK: Filter 'Semua Zona' berhasil mengembalikan seluruh destinasi")

        # -------------------------------------------------------------
        # UJI 4: VALIDASI DAN PENGIRIMAN FORMULIR KONTAK
        # -------------------------------------------------------------
        print("\n[UJI 4] Verifikasi Interaksi Formulir Reservasi...")
        page.goto(kontak_url)
        
        # Mengisi formulir dengan data valid
        page.fill("#input-nama", "Hadi Sulaiman")
        page.fill("#input-email", "hadi.sulaiman@unpam.ac.id")
        page.fill("#input-telepon", "085150299425")
        page.select_option("#input-destinasi", "raja-ampat")
        page.fill("#input-peserta", "Rombongan 4 orang mahasiswa Teknik Informatika")
        
        # Submit form
        page.locator("button[type='submit']").click()
        
        # Verifikasi alert status sukses muncul
        alert = page.locator("#form-alert")
        assert alert.is_visible(), "Alert sukses form harus ditampilkan"
        print("  OK: Pengiriman Formulir Reservasi memunculkan status sukses terverifikasi")

        # -------------------------------------------------------------
        # UJI 5: VERIFIKASI LOGO PINISI DAN AUDIT STANDAR ANTI-SLOP
        # -------------------------------------------------------------
        print("\n[UJI 5] Audit Standar Kualitas Anti-Slop & Desain Logo...")
        
        # Verifikasi Logo Pinisi ada di header
        page.goto(index_url)
        logo = page.locator(".logo-pinisi")
        assert logo.is_visible(), "Logo Kapal Pinisi harus tampil jelas di header"
        print("  OK: Logo Kapal Pinisi Tradisional terverifikasi tampil jelas")
        
        for fname in ["index.html", "destinasi.html", "paket.html", "kontak.html"]:
            fpath = os.path.join(base_dir, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Larangan Em Dash (R-02)
            assert "—" not in content, f"Pelanggaran R-02: Karakter em dash ditemukan di {fname}"
            
            # Larangan AI Marketing Buzzwords (R-16)
            for buzzword in ["AI Powered", "Revolutionary", "Next Generation", "Cutting Edge"]:
                assert buzzword not in content, f"Pelanggaran R-16: Kata klise '{buzzword}' ditemukan di {fname}"
                
            print(f"  OK: Berkas {fname} bebas em dash dan bebas kata klise AI")

        browser.close()

    print("\n======================================================================")
    print(" SEMUA PENGUJIAN END-TO-END (E2E) LULUS 100% (ALL SUITES PASSED)")
    print("======================================================================")

if __name__ == "__main__":
    run_e2e()
