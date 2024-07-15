import streamlit as st
import pandas as pd

# Data JSON yang disimpan dalam variabel Python
data_json = [
    {
        "kategori": "Fiksi",
        "buku": [
            {"judul": "Buku Fiksi 1", "pengarang": "Pengarang 1", "penerbit": "Penerbit 1", "tahun_terbit": 2020, "lantai": 1, "ruangan": "A", "rak": 1},
            {"judul": "Buku Fiksi 2", "pengarang": "Pengarang 2", "penerbit": "Penerbit 2", "tahun_terbit": 2021, "lantai": 1, "ruangan": "A", "rak": 2}
        ]
    },
    {
        "kategori": "Non-Fiksi",
        "buku": [
            {"judul": "Buku Non-Fiksi 1", "pengarang": "Pengarang 3", "penerbit": "Penerbit 3", "tahun_terbit": 2019, "lantai": 2, "ruangan": "B", "rak": 3},
            {"judul": "Buku Non-Fiksi 2", "pengarang": "Pengarang 4", "penerbit": "Penerbit 4", "tahun_terbit": 2018, "lantai": 2, "ruangan": "B", "rak": 4}
        ]
    }
]

# Fungsi untuk mencari buku berdasarkan kategori
def cari_buku(kategori_dicari, data):
    for kategori in data:
        if kategori['kategori'].lower() == kategori_dicari.lower():
            return kategori['buku']
    return None

# Pengaturan tampilan
st.set_page_config(
    page_title="Pencarian Buku Perpustakaan",
    layout="wide"
)

# Sidebar
st.sidebar.header("Pencarian Buku")
st.sidebar.markdown("""
Gunakan aplikasi ini untuk mencari lokasi buku di perpustakaan.  
Pilih kategori buku pada kolom di bawah dan tekan tombol 'Cari'.
""")

# Judul aplikasi
st.title("📚 Pencarian Buku Perpustakaan")

# Data perpustakaan dari variabel langsung
data_perpustakaan = data_json

# Jika data berhasil dibaca
if data_perpustakaan:
    # Ambil daftar kategori buku
    daftar_kategori = ["Pilih kategori buku"] + [kategori['kategori'] for kategori in data_perpustakaan]

    # Input pengguna
    kategori_yang_dicari = st.selectbox("Pilih Kategori Buku:", daftar_kategori)

    # Tombol untuk mencari
    if st.button("Cari"):
        if kategori_yang_dicari != "Pilih kategori buku":
            # Cari buku berdasarkan kategori yang dipilih
            buku_ditemukan = cari_buku(kategori_yang_dicari, data_perpustakaan)
            
            # Buat DataFrame untuk menampilkan hasil
            if buku_ditemukan:
                df = pd.DataFrame(buku_ditemukan)
                df['No'] = range(1, len(df) + 1)  # Tambah kolom No dengan nomor urut dimulai dari 1
                df = df.rename(columns={'judul': 'Judul', 'pengarang': 'Pengarang', 
                                        'penerbit': 'Penerbit', 'tahun_terbit': 'Tahun Terbit',
                                        'lantai': 'Lantai', 'ruangan': 'Ruangan', 'rak': 'Rak'})
                df = df[['No', 'Judul', 'Pengarang', 'Penerbit', 'Tahun Terbit', 'Lantai', 'Ruangan', 'Rak']]  # Susun ulang kolom
                st.subheader(f"Buku-buku dalam kategori '{kategori_yang_dicari}':")
                st.write(df.to_html(index=False), unsafe_allow_html=True)  # Tampilkan tabel tanpa indeks
            else:
                st.warning("Tidak ada buku yang ditemukan dalam kategori ini.")
        else:
            st.warning("Silakan pilih kategori buku.")
else:
    st.error("Data perpustakaan tidak tersedia.")
