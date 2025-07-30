import streamlit as st

# 🎨 Styling CSS
st.markdown("""
    <style>
        html, body, .main {
            background-color: #f7f9fc;
            font-family: 'Segoe UI', sans-serif;
        }

        h1, h2, h3, .stTitle {
            color: #2C3E50;
        }

        .stButton > button {
            background-color: #2C3E50;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            transition: 0.3s ease;
        }

        .stButton > button:hover {
            background-color: #34495E;
            color: #ecf0f1;
        }

        .stTextInput > div > input,
        .stNumberInput input {
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 10px;
        }

        .stSelectbox > div {
            border-radius: 10px;
        }

        .stAlert {
            border-radius: 10px !important;
            background-color: #EAF2F8;
            color: #154360;
        }

        .block-container {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# 📘 Kelas Buku
class Buku:
    def __init__(self, kode, judul, penulis, tahun):
        self.kode = kode
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def __str__(self):
        return f"[{self.kode}] {self.judul} oleh {self.penulis} ({self.tahun})"

# 📂 Inisialisasi data
if 'data_buku' not in st.session_state:
    st.session_state.data_buku = []

# 🧾 Tampilan utama
st.title("📚 Aplikasi CRUD Data Buku")

menu = st.selectbox("📌 Pilih Menu", ["Lihat Buku", "Tambah Buku", "Ubah Buku", "Hapus Buku"])

# 📄 LIHAT DATA
if menu == "Lihat Buku":
    st.subheader("📖 Daftar Buku")
    if st.session_state.data_buku:
        for i, buku in enumerate(st.session_state.data_buku):
            st.write(f"{i+1}. {buku}")
    else:
        st.info("Belum ada data buku.")

# ➕ TAMBAH DATA
elif menu == "Tambah Buku":
    st.subheader("📝 Tambah Buku Baru")
    kode = st.text_input("Kode Buku")
    judul = st.text_input("Judul Buku")
    penulis = st.text_input("Penulis")
    tahun = st.text_input("Tahun Terbit")
    if st.button("Simpan"):
        if kode and judul and penulis and tahun:
            buku = Buku(kode, judul, penulis, tahun)
            st.session_state.data_buku.append(buku)
            st.success("✅ Buku berhasil ditambahkan.")
        else:
            st.warning("⚠️ Harap isi semua kolom.")

# ✏️ UBAH DATA
elif menu == "Ubah Buku":
    st.subheader("✏️ Ubah Data Buku")
    data = st.session_state.data_buku
    if data:
        indeks = st.number_input("Masukkan nomor buku yang ingin diubah:", min_value=1, max_value=len(data))
        selected = data[indeks - 1]
        new_kode = st.text_input("Ubah Kode Buku", selected.kode)
        new_judul = st.text_input("Ubah Judul Buku", selected.judul)
        new_penulis = st.text_input("Ubah Penulis", selected.penulis)
        new_tahun = st.text_input("Ubah Tahun Terbit", selected.tahun)
        if st.button("Update"):
            if new_kode and new_judul and new_penulis and new_tahun:
                st.session_state.data_buku[indeks - 1] = Buku(new_kode, new_judul, new_penulis, new_tahun)
                st.success("✅ Data buku berhasil diubah.")
            else:
                st.warning("⚠️ Harap isi semua kolom.")
    else:
        st.info("Belum ada data buku.")

# 🗑️ HAPUS DATA
elif menu == "Hapus Buku":
    st.subheader("🗑️ Hapus Buku")
    data = st.session_state.data_buku
    if data:
        indeks = st.number_input("Masukkan nomor buku yang ingin dihapus:", min_value=1, max_value=len(data))
        if st.button("Hapus"):
            deleted = st.session_state.data_buku.pop(indeks - 1)
            st.success(f"✅ Buku '{deleted.judul}' berhasil dihapus.")
    else:
        st.info("Belum ada data buku.")
