"""
Skrip Pengujian Otomatis Kepatuhan Layout DIV dan CSS Sesuai Variasi NIM 241011402572
Penugasan: Pemrograman Web 1 - Universitas Pamulang
"""

from playwright.sync_api import sync_playwright
import os
import sys

def run_tests():
    print("==================================================================")
    print(" MEMULAI PENGUJIAN OTOMATIS: LAYOUT DIV & CSS BERDASARKAN NIM")
    print(" Mahasiswa: Hadi Sulaiman | NIM: 241011402572")
    print("==================================================================")
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = f"file:///{os.path.join(current_dir, 'index.html').replace(os.sep, '/')}"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='msedge')
        page = browser.new_page(viewport={'width': 1200, 'height': 1400})
        page.goto(index_path)
        
        # 1. Uji Wrapper
        wrapper = page.locator("#wrapper")
        wrapper_box = wrapper.bounding_box()
        print(f"\n[1] PENGUJIAN LEBAR WRAPPER:")
        print(f"    - Nilai Eksak Target: 840px (700 + 7x20)")
        print(f"    - Hasil Terukur     : {wrapper_box['width']}px")
        assert abs(wrapper_box['width'] - 840) < 2, f"Lebar wrapper tidak sesuai: {wrapper_box['width']}"
        print("    -> STATUS: LULUS (PASS)")

        # 2. Uji Header
        header = page.locator("#header")
        header_box = header.bounding_box()
        print(f"\n[2] PENGUJIAN TINGGI HEADER:")
        print(f"    - Nilai Eksak Target: 100px (80 + 2x10)")
        print(f"    - Hasil Terukur     : {header_box['height']}px")
        assert abs(header_box['height'] - 100) < 2, f"Tinggi header tidak sesuai: {header_box['height']}"
        print("    -> STATUS: LULUS (PASS)")

        # 3. Uji Sidebar Kiri
        sidebar = page.locator("#sidebar")
        sidebar_box = sidebar.bounding_box()
        print(f"\n[3] PENGUJIAN SIDEBAR KIRI:")
        print(f"    - Lebar Terukur: {sidebar_box['width']}px (~25% area utama)")
        assert sidebar_box['width'] > 180 and sidebar_box['width'] <= 215, "Lebar sidebar di luar batas proporsional 25%"
        print("    -> STATUS: LULUS (PASS)")

        # 4. Uji Jarak Margin Antarkolom
        content = page.locator("#content")
        content_box = content.bounding_box()
        col_gap = content_box['x'] - (sidebar_box['x'] + sidebar_box['width'])
        print(f"\n[4] PENGUJIAN JARAK MARGIN ANTARKOLOM (Sidebar & Content):")
        print(f"    - Nilai Eksak Target: 14px (7 x 2)")
        print(f"    - Hasil Terukur     : {col_gap}px")
        assert abs(col_gap - 14) < 2, f"Jarak margin antarkolom tidak sesuai: {col_gap}"
        print("    -> STATUS: LULUS (PASS)")

        # 5. Uji Dua Bagian Content (Kolom 1 & Kolom 2)
        col1 = page.locator("#content-kolom-1")
        col2 = page.locator("#content-kolom-2")
        box1 = col1.bounding_box()
        box2 = col2.bounding_box()
        inner_gap = box2['x'] - (box1['x'] + box1['width'])
        print(f"\n[5] PENGUJIAN JARAK MARGIN CONTENT DUA BAGIAN:")
        print(f"    - Nilai Eksak Target: 14px (7 x 2)")
        print(f"    - Hasil Terukur     : {inner_gap}px")
        assert abs(inner_gap - 14) < 2, f"Jarak antarkolom content dua bagian tidak sesuai: {inner_gap}"
        print("    -> STATUS: LULUS (PASS)")

        # 6. Uji Tinggi Minimum Content
        content_height = content_box['height']
        print(f"\n[6] PENGUJIAN TINGGI MINIMUM CONTENT:")
        print(f"    - Nilai Minimum Target: 240px (200 + 2x20)")
        print(f"    - Hasil Terukur       : {content_height}px")
        assert content_height >= 240, f"Tinggi content kurang dari 240px: {content_height}"
        print("    -> STATUS: LULUS (PASS)")

        # 7. Uji Keberadaan Tag DIV Pembentuk Struktur
        div_count = page.locator("div").count()
        print(f"\n[7] PENGUJIAN ELEMEN STRUKTUR TAG <DIV>:")
        print(f"    - Total Tag <div> Ditemukan: {div_count}")
        assert div_count >= 15, "Tag <div> kurang untuk membentuk struktur layout lengkap"
        print("    -> STATUS: LULUS (PASS)")

        browser.close()

    print("\n==================================================================")
    print(" SELURUH PENGUJIAN BERHASIL 100% (ALL TESTS PASSED)!")
    print("==================================================================")

if __name__ == "__main__":
    run_tests()
