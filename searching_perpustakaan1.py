import streamlit as st
import pandas as pd

# Data JSON yang disimpan dalam variabel Python
data_json = [
    {
        "kategori": "Program komputer",
        "buku": [
            {
                "judul": "Belajar Python 3",
                "pengarang": "Dian Lesmana, M.T",
                "penerbit": "Penerbit Andi",
                "tahun_terbit": "2018",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "005"
            },
            {
                "judul": "Algoritma dan Pemrograman dengan Python",
                "pengarang": "Aditya Suranata, S.Kom.,M.T.I",
                "penerbit": "Penerbit Andi",
                "tahun_terbit": "2020",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "006"
            },
            {
                "judul": "Algoritma dan Struktur Data dalam Bahasa Java",
                "pengarang": "Rinaldi Munir",
                "penerbit": "Informatika",
                "tahun_terbit": "2010",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "007"
            },
            {
                "judul": "Pemrograman Basis Data dengan MySQL",
                "pengarang": "Iwan Nur Fadillah",
                "penerbit": "Penerbit Andi",
                "tahun_terbit": "2016",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "008"
            },
            {
                "judul": "Pemrograman Java untuk Pemula",
                "pengarang": "Bambang Hariyanto",
                "penerbit": "Elex Media Komputindo",
                "tahun_terbit": "2017",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "010"
            }
        ]
    },
    {
        "kategori": "Filsafat",
        "buku": [
            {
                "judul": "Filsafat",
                "pengarang": "Jane Smith",
                "penerbit": "Penerbit B",
                "tahun_terbit": "2012",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "100"
            },
            {
                "judul": "Pemikiran",
                "pengarang": "Michael Johnson",
                "penerbit": "Penerbit C",
                "tahun_terbit": "2013",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "101"
            },
            {
                "judul": "Etika",
                "pengarang": "Alice Brown",
                "penerbit": "Penerbit D",
                "tahun_terbit": "2015",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "102"
            },
            {
                "judul": "Logika",
                "pengarang": "Robert Davis",
                "penerbit": "Penerbit E",
                "tahun_terbit": "2017",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "103"
            },
            {
                "judul": "Metafisika",
                "pengarang": "Laura Wilson",
                "penerbit": "Penerbit F",
                "tahun_terbit": "2019",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "104"
            }
        ]
    },
    {
        "kategori": "Sosiologi",
        "buku": [
            {
                "judul": "Sosiologi",
                "pengarang": "William Taylor",
                "penerbit": "Penerbit G",
                "tahun_terbit": "2011",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "301"
            },
            {
                "judul": "Masyarakat",
                "pengarang": "Charles Green",
                "penerbit": "Penerbit H",
                "tahun_terbit": "2014",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "302"
            },
            {
                "judul": "Interaksi Sosial",
                "pengarang": "Kevin Harris",
                "penerbit": "Penerbit I",
                "tahun_terbit": "2016",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "303"
            },
            {
                "judul": "Kelas Sosial",
                "pengarang": "Elizabeth Clark",
                "penerbit": "Penerbit J",
                "tahun_terbit": "2018",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "304"
            },
            {
                "judul": "Fenomena Sosial",
                "pengarang": "Thomas Moore",
                "penerbit": "Penerbit K",
                "tahun_terbit": "2020",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "305"
            }
        ]
    },
    {
        "kategori": "Hukum",
        "buku": [
            {
                "judul": "Hukum Pidana",
                "pengarang": "Michael Brown",
                "penerbit": "Penerbit L",
                "tahun_terbit": "2012",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "340"
            },
            {
                "judul": "Hukum Perdata",
                "pengarang": "Emily Davis",
                "penerbit": "Penerbit M",
                "tahun_terbit": "2013",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "341"
            },
            {
                "judul": "Hukum Internasional",
                "pengarang": "Robert Wilson",
                "penerbit": "Penerbit N",
                "tahun_terbit": "2015",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "342"
            },
            {
                "judul": "Hukum Keluarga",
                "pengarang": "Laura Martinez",
                "penerbit": "Penerbit O",
                "tahun_terbit": "2017",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "343"
            },
            {
                "judul": "Hukum Bisnis",
                "pengarang": "James Anderson",
                "penerbit": "Penerbit P",
                "tahun_terbit": "2019",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "344"
            }
        ]
    },
    {
        "kategori": "Kesehatan",
        "buku": [
            {
                "judul": "Kesehatan",
                "pengarang": "William Thomas",
                "penerbit": "Penerbit Q",
                "tahun_terbit": "2011",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "610"
            },
            {
                "judul": "Nutrisi",
                "pengarang": "Sarah Walker",
                "penerbit": "Penerbit R",
                "tahun_terbit": "2014",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "611"
            },
            {
                "judul": "Penyakit Umum",
                "pengarang": "Daniel Hall",
                "penerbit": "Penerbit S",
                "tahun_terbit": "2016",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "612"
            },
            {
                "judul": "Kesehatan Mental",
                "pengarang": "Jessica Perez",
                "penerbit": "Penerbit T",
                "tahun_terbit": "2018",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "613"
            },
            {
                "judul": "Kesehatan Lingkungan",
                "pengarang": "David Garcia",
                "penerbit": "Penerbit U",
                "tahun_terbit": "2020",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "614"
            }
        ]
    },
    {
        "kategori": "Agrobisnis",
        "buku": [
            {
                "judul": "Pertanian",
                "pengarang": "Charles Jackson",
                "penerbit": "Penerbit V",
                "tahun_terbit": "2013",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "631"
            },
            {
                "judul": "Agribisnis",
                "pengarang": "Richard White",
                "penerbit": "Penerbit W",
                "tahun_terbit": "2015",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "632"
            },
            {
                "judul": "Hortikultura",
                "pengarang": "Susan Harris",
                "penerbit": "Penerbit X",
                "tahun_terbit": "2017",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "633"
            },
            {
                "judul": "Peternakan",
                "pengarang": "Matthew Clark",
                "penerbit": "Penerbit Y",
                "tahun_terbit": "2019",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "634"
            },
            {
                "judul": "Agronomi",
                "pengarang": "Jessica King",
                "penerbit": "Penerbit Z",
                "tahun_terbit": "2021",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "635"
            }
        ]
    },
    {
        "kategori": "Teknik",
        "buku": [
            {
                "judul": "Teknik",
                "pengarang": "Henry Lee",
                "penerbit": "Penerbit A1",
                "tahun_terbit": "2014",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "621"
            },
            {
                "judul": "Engineering",
                "pengarang": "Kevin Moore",
                "penerbit": "Penerbit B1",
                "tahun_terbit": "2016",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "622"
            },
            {
                "judul": "Konstruksi",
                "pengarang": "Emily Taylor",
                "penerbit": "Penerbit C1",
                "tahun_terbit": "2018",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "623"
            },
            {
                "judul": "Manufaktur",
                "pengarang": "Laura Martin",
                "penerbit": "Penerbit D1",
                "tahun_terbit": "2020",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "624"
            },
            {
                "judul": "Robotik",
                "pengarang": "James Allen",
                "penerbit": "Penerbit E1",
                "tahun_terbit": "2022",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "625"
            }
        ]
    },
    {
        "kategori": "Peternakan",
        "buku": [
            {
                "judul": "Peternakan",
                "pengarang": "Thomas Perez",
                "penerbit": "Penerbit F1",
                "tahun_terbit": "2016",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "636"
            },
            {
                "judul": "Ternak Unggas",
                "pengarang": "David Walker",
                "penerbit": "Penerbit G1",
                "tahun_terbit": "2018",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "637"
            },
            {
                "judul": "Pemuliaan Hewan",
                "pengarang": "Jessica Harris",
                "penerbit": "Penerbit H1",
                "tahun_terbit": "2020",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "638"
            },
            {
                "judul": "Kesehatan Hewan",
                "pengarang": "Robert Perez",
                "penerbit": "Penerbit I1",
                "tahun_terbit": "2022",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "639"
            },
            {
                "judul": "Manajemen Peternakan",
                "pengarang": "Elizabeth Clark",
                "penerbit": "Penerbit J1",
                "tahun_terbit": "2024",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "640"
            }
        ]
    },
    {
        "kategori": "Komputer Pengolahan Data",
        "buku": [
            {
                "judul": "Komputer",
                "pengarang": "Kevin White",
                "penerbit": "Penerbit K1",
                "tahun_terbit": "2018",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "004"
            },
            {
                "judul": "Data Science",
                "pengarang": "Michael Green",
                "penerbit": "Penerbit L1",
                "tahun_terbit": "2020",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "005"
            },
            {
                "judul": "Pemrograman",
                "pengarang": "Robert Walker",
                "penerbit": "Penerbit M1",
                "tahun_terbit": "2022",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "006"
            },
            {
                "judul": "Artificial Intelligence",
                "pengarang": "Jessica Moore",
                "penerbit": "Penerbit N1",
                "tahun_terbit": "2024",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "007"
            },
            {
                "judul": "Cybersecurity",
                "pengarang": "Daniel Harris",
                "penerbit": "Penerbit O1",
                "tahun_terbit": "2026",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "008"
            }
        ]
    },
    {
        "kategori": "Komunikasi",
        "buku": [
            {
                "judul": "Komunikasi",
                "pengarang": "Elizabeth Harris",
                "penerbit": "Penerbit P1",
                "tahun_terbit": "2019",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "001"
            },
            {
                "judul": "Public Speaking",
                "pengarang": "Thomas Anderson",
                "penerbit": "Penerbit Q1",
                "tahun_terbit": "2021",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "002"
            },
            {
                "judul": "Media Sosial",
                "pengarang": "Jessica King",
                "penerbit": "Penerbit R1",
                "tahun_terbit": "2023",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "003"
            },
            {
                "judul": "Jurnalisme",
                "pengarang": "Robert Clark",
                "penerbit": "Penerbit S1",
                "tahun_terbit": "2025",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "004"
            },
            {
                "judul": "Komunikasi Bisnis",
                "pengarang": "Laura Brown",
                "penerbit": "Penerbit T1",
                "tahun_terbit": "2027",
                "lantai": 1,
                "ruangan": "Koleksi",
                "rak": "005"
            }
        ]
    },
    {
        "kategori": "Kamus Sains",
        "buku": [
            {
                "judul": "Sains",
                "pengarang": "David Clark",
                "penerbit": "Penerbit U1",
                "tahun_terbit": "2012",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "503"
            },
            {
                "judul": "Scientific Method",
                "pengarang": "Susan Walker",
                "penerbit": "Penerbit V1",
                "tahun_terbit": "2014",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "504"
            },
            {
                "judul": "Biology",
                "pengarang": "Richard Taylor",
                "penerbit": "Penerbit W1",
                "tahun_terbit": "2016",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "505"
            },
            {
                "judul": "Chemistry",
                "pengarang": "Edward Harris",
                "penerbit": "Penerbit X1",
                "tahun_terbit": "2018",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "506"
            },
            {
                "judul": "Physics",
                "pengarang": "Jessica Clark",
                "penerbit": "Penerbit Y1",
                "tahun_terbit": "2020",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "507"
            }
        ]
    },
    {
        "kategori": "Ensiklopedia",
        "buku": [
            {
                "judul": "Referensi",
                "pengarang": "Susan Lewis",
                "penerbit": "Penerbit Z1",
                "tahun_terbit": "2014",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "501"
            },
            {
                "judul": "Knowledge",
                "pengarang": "John Anderson",
                "penerbit": "Penerbit A2",
                "tahun_terbit": "2016",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "502"
            },
            {
                "judul": "World",
                "pengarang": "Emily Perez",
                "penerbit": "Penerbit B2",
                "tahun_terbit": "2018",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "503"
            },
            {
                "judul": "Encyclopedia",
                "pengarang": "David Brown",
                "penerbit": "Penerbit C2",
                "tahun_terbit": "2020",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "504"
            },
            {
                "judul": "Universe",
                "pengarang": "Jessica Wilson",
                "penerbit": "Penerbit D2",
                "tahun_terbit": "2022",
                "lantai": 2,
                "ruangan": "Referensi",
                "rak": "505"
            }
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
