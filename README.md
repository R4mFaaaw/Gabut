# MINERAPETRO-EXPERT: Platform Interaktif & Media Hafalan Praktikum Mineralogi & Petrologi

**Program Studi S1 Teknik Pertambangan | Fakultas Teknik | Universitas Kutai Kartanegara (UNIKARTA)**  
*Dosen Pengampu: **Sundyo, S.T., M.T.***  
*Asisten Praktikum: **1. Al Disa Eka Saputri** & **2. Amalia Azis***

---

## 💎 Pengantar dari Dosen Pengampu

> *"Selamat datang mahasiswa Teknik Pertambangan! Di dalam industri pertambangan modern, pemahaman mengenai mineralogi dan petrologi bukan sekadar teori di atas kertas. Identifikasi mineral menentukan kadar bijih ekonomis (*ore grade*), alterasi hidrotermal, hingga kestabilan lereng tambang (*slope stability*). Gunakan platform ini untuk melatih ingatan hafalan Anda secara mendalam sebelum mengikuti responsi laboratorium."*  
> — **Sundyo, S.T., M.T.**

---

## 🚀 Fitur Unggulan Aplikasi (Full-Stack & Animated)

1. **Kanvas Animasi Poligon Kristal Dinamis (Canvas Background)**:
   - Kristal mengapung dengan geometri heksagonal dan isometrik kubik yang bergerak halus di latar belakang.
2. **Audio Synthesizer Web Audio API Terintegrasi**:
   - Efek suara sintetis tanpa memerlukan aset audio eksternal: klik tombol, efek suara gesekan kartu 3D, akord nada mayor untuk jawaban benar, buzzer nada rendah untuk jawaban salah, dan melodi kemenangan/fanfare.
3. **Fitur Text-to-Speech Suara Dosen (Web Speech API)**:
   - Dosen memberikan pengantar dan tips belajar langsung dalam bahasa Indonesia.
4. **9 Bab Kuliah Interaktif Lengkap**:
   - **Modul 00**: Tata Tertib Lab (13 Kewajiban, 4 Larangan, 5 Kriteria Sanksi A-E).
   - **Modul 01**: Mineralogi Dasar & Genesa Mineral (Magmatik, Metamorfosa, Sedimen, dan 10 proses keterbentukan).
   - **Modul 02**: Sifat Fisik Mineral & Skala Mohs (8 Kilap, 5 Pecahan, 6 Belahan, Tenacity, dan Uji Lapangan).
   - **Modul 03**: Bentuk Kristal & 7 Sistem Kristalografi (Rasio sumbu, sudut, dan contoh mineral).
   - **Modul 04**: Mineral Silika vs Non-Silika (Ferromagnesian, variasi Kuarsa, dan 7 kelas Non-Silika).
   - **Modul 05**: Petrologi Umum & Batuan Beku (Tekstur mikroskopis, klasifikasi warna mafik, dan kadar SiO2).
   - **Modul 06**: Batuan Sedimen Klastik & Non-Klastik (Skala Wentworth, kemas, porositas, dan 6 golongan Koesoemadinata).
   - **Modul 07**: Struktur Batuan Sedimen Lengkap (Graded Bedding, Cross Bedding, Flute Cast, Flame Structure, dll.).
   - **Modul 08**: Batuan Metamorf (Struktur Foliasi, Non-Foliasi, dan Tekstur Kristaloblastik).
5. **Flashcards 3D Interaktif (Metode Spaced Repetition)**:
   - Kartu 3D dengan efek rotasi realistis (*preserve-3d*).
   - Tombol **"Sudah Hafal"** dan **"Belum Hafal"** yang tersimpan di `localStorage` peramban.
   - Filter kartu per bab materi.
   - Navigasi keyboard: `[Spasi]` untuk membalik kartu, `[←]` dan `[→]` untuk berganti kartu.
6. **Mini-Game Lab Skala Mohs (Interactive Ordering Drill)**:
   - Menyusun 10 mineral dari yang paling lunak ke paling keras beserta rumus kimianya.
   - Dilengkapi panduan alat uji lapangan (kuku, jarum, uang koin, pisau baja, kaca, kikir, ampelas).
   - Pengecekan otomatis dengan efek konfeti emas saat nilai 10/10 tercapai.
7. **Simulator Responsi Laboratorium (60 Soal Bank Pertanyaan)**:
   - 3 Mode: **Pre-Test Cepat (10 Soal)**, **Responsi Standar (25 Soal)**, dan **Ujian Komprehensif (60 Soal)**.
   - Pilihan ganda acak dengan pembahasan langsung dari halaman modul resmi.
   - Kartu Hasil Ujian Digital dengan Grade (A, B, C, D/E), evaluasi dosen, dan fitur cetak lembar hasil.
8. **Kamus Glosarium Cepat Tambang**:
   - Pencarian instan istilah-istilah kunci untuk persiapan ujian responsi.

---

## 🛠️ Cara Menjalankan Aplikasi

### Opsi 1: Menjalankan Langsung di Browser
Cukup buka file `index.html` menggunakan peramban favorit Anda (Google Chrome, Mozilla Firefox, Microsoft Edge, Safari):
```bash
# Di Linux / Ubuntu
xdg-open index.html
```

### Opsi 2: Menggunakan Web Server Lokal (Direkomendasikan)
Gunakan script pembantu yang telah disediakan:
```bash
chmod +x run.sh
./run.sh
```
Atau via Python standar:
```bash
python3 -m http.server 8080
```
Buka peramban di `http://localhost:8080/`.

---

## 📂 Struktur Berkas

- `index.html` : Struktur antarmuka web semantik dan tata letak responsif.
- `style.css` : Sistem desain pertambangan modern, animasi kristal, kartu 3D, dan glassmorphism.
- `app.js` : Engine interaktif, Web Audio synthesizer, canvas partikel, confetti, logika flashcards, mini-game Mohs, dan simulator responsi.
- `data.js` : Basis data komprehensif seluruh modul, 60 kartu hafalan, 60 bank soal kuis, rumus kimia, dan glosarium.
- `run.sh` : Script peluncur server web lokal otomatis.
- `MODUL PRAKTIKUM MATKUL MINERALOGI & PETROLOGI.pdf` : Dokumen sumber modul resmi praktikum FT-UNIKARTA.

---
*Dibuat untuk kemajuan akademik mahasiswa Teknik Pertambangan Fakultas Teknik Universitas Kutai Kartanegara.*
