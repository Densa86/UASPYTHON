import streamlit as st

# ========== CSS ========== #
st.markdown("""
    <style>
    /* Background gradasi */
    .stApp {
        background: linear-gradient(to bottom right, #E0EAFC, #CFDEF3);
        font-family: 'Segoe UI', sans-serif;
        color: #333333;
    }

    /* Judul aplikasi */
    h1 {
        color: #005c97;
        text-shadow: 1px 1px 2px #ccc;
    }

    /* Subheader */
    h2, h3 {
        color: #007acc;
    }

    /* Card effect */
    .stMarkdown, .stTextInput, .stTextArea, .stNumberInput, .stButton, .stSelectbox {
        background-color: #ffffffcc;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }

    /* Placeholder style */
    input::placeholder, textarea::placeholder {
        color: #888 !important;
        font-style: italic;
    }

    /* Button styling */
    button {
        background-color: #007acc !important;
        color: white !important;
        border-radius: 8px;
    }

    button:hover {
        background-color: #005c97 !important;
    }

    /* Info box */
    .stAlert {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ========== Class Mahasiswa ========== #
class Mahasiswa:
    def __init__(self, nim, nama, no_hp, email, alamat):
        self.nim = nim
        self.nama = nama
        self.no_hp = no_hp
        self.email = email
        self.alamat = alamat

    def __str__(self):
        return (
            f"NIM: {self.nim}, Nama: {self.nama}, "
            f"No HP: {self.no_hp}, Email: {self.email}, Alamat: {self.alamat}"
        )

# ========== Inisialisasi Data ========== #
if 'data_mahasiswa' not in st.session_state:
    st.session_state.data_mahasiswa = []

# ========== Tampilan Utama ========== #
st.title("📚 MyStudent Manager")
st.write("### Silakan pilih menu di bawah ini:")

menu = st.selectbox("Pilih Menu:", ["Lihat Data", "Tambah Data", "Ubah Data", "Hapus Data"])

# ========== Menu: Lihat Data ========== #
if menu == "Lihat Data":
    st.subheader("📄 Daftar Mahasiswa")
    if st.session_state.data_mahasiswa:
        for i, mhs in enumerate(st.session_state.data_mahasiswa):
            st.markdown(f"**{i+1}. {mhs}**")
    else:
        st.info("Belum ada data.")

# ========== Menu: Tambah Data ========== #
elif menu == "Tambah Data":
    st.subheader("➕ Tambah Mahasiswa")
    nim = st.text_input("Masukkan NIM", placeholder="Contoh: 24.02.1107")
    nama = st.text_input("Masukkan Nama", placeholder="Contoh: Raden Said")
    no_hp = st.text_input("Masukkan No HP", placeholder="Contoh: 081234567890")
    email = st.text_input("Masukkan Email", placeholder="Contoh: saidygy@gmail.com")
    alamat = st.text_area("Masukkan Alamat", placeholder="Contoh: kwarakan,sidorejo,lendah,kulon progo,D.I. Yogyakarta")
    if st.button("Simpan"):
        if nim and nama and no_hp and email and alamat:
            mhs = Mahasiswa(nim, nama, no_hp, email, alamat)
            st.session_state.data_mahasiswa.append(mhs)
            st.success("✅ Data berhasil disimpan!")
        else:
            st.warning("⚠️ Mohon isi semua field!")

# ========== Menu: Ubah Data ========== #
elif menu == "Ubah Data":
    st.subheader("✏️ Ubah Data Mahasiswa")
    if st.session_state.data_mahasiswa:
        idx = st.number_input("Pilih nomor data yang ingin diubah:", min_value=1, max_value=len(st.session_state.data_mahasiswa))
        selected = st.session_state.data_mahasiswa[idx-1]

        new_nim = st.text_input("NIM Baru", value=selected.nim, placeholder="Contoh: 22010001")
        new_nama = st.text_input("Nama Baru", value=selected.nama, placeholder="Contoh: Budi Santoso")
        new_no_hp = st.text_input("No HP Baru", value=selected.no_hp, placeholder="Contoh: 081234567890")
        new_email = st.text_input("Email Baru", value=selected.email, placeholder="Contoh: budi@email.com")
        new_alamat = st.text_area("Alamat Baru", value=selected.alamat, placeholder="Contoh: Jl. Melati No. 5, Jakarta")

        if st.button("Ubah"):
            selected.nim = new_nim
            selected.nama = new_nama
            selected.no_hp = new_no_hp
            selected.email = new_email
            selected.alamat = new_alamat
            st.success("✅ Data berhasil diubah!")
    else:
        st.info("Belum ada data.")

# ========== Menu: Hapus Data ========== #
elif menu == "Hapus Data":
    st.subheader("🗑️ Hapus Data Mahasiswa")
    if st.session_state.data_mahasiswa:
        idx = st.number_input("Pilih nomor data yang ingin dihapus:", min_value=1, max_value=len(st.session_state.data_mahasiswa))
        if st.button("Hapus"):
            deleted = st.session_state.data_mahasiswa.pop(idx-1)
            st.success(f"✅ Data {deleted.nama} berhasil dihapus!")
    else:
        st.info("Belum ada data.")
