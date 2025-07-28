import streamlit as st

# ================== CSS Tampilan Elegan ==================
st.markdown("""
    <style>
    /* Background dan font */
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', sans-serif;
        color: #1C1C1C;
        padding: 10px;
    }

    /* Judul */
    h1 {
        color: #2E86C1;
        font-weight: bold;
        font-size: 36px;
        padding-bottom: 10px;
    }

    /* Subjudul */
    h3 {
        color: #1C1C1C;
        font-weight: 600;
        margin-top: 10px;
    }

    /* Input */
    .stTextInput>div>div>input, .stTextArea textarea {
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 6px;
        background-color: #ffffff;
        color: #1C1C1C;
    }

    /* Tombol */
    .stButton>button {
        background-color: #3498DB;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        border: none;
        transition: background-color 0.3s ease;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #2E86C1;
    }

    /* Info Box */
    .stAlert {
        background-color: #EBF5FB;
        padding: 1rem;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# ================== Kelas Mahasiswa ==================
class Mahasiswa:
    def __init__(self, nim, nama, no_hp, email, alamat):
        self.nim = nim
        self.nama = nama
        self.no_hp = no_hp
        self.email = email
        self.alamat = alamat

    def __str__(self):
        return (f"NIM: {self.nim}, Nama: {self.nama}, No HP: {self.no_hp}, "
                f"Email: {self.email}, Alamat: {self.alamat}")

# ================== Data Session State ==================
if 'data_mahasiswa' not in st.session_state:
    st.session_state.data_mahasiswa = []

# ================== Tampilan Utama ==================
st.title("📘 Aplikasi CRUD Mahasiswa")

st.write("### Pilihan Menu:")
st.write("1. Lihat Data")
st.write("2. Tambah Data")
st.write("3. Ubah Data")
st.write("4. Hapus Data")

menu = st.text_input("Masukkan angka menu (1-4):")

# ================== Lihat Data ==================
if menu == "1":
    st.subheader("📄 Daftar Mahasiswa")
    if st.session_state.data_mahasiswa:
        for i, mhs in enumerate(st.session_state.data_mahasiswa):
            st.markdown(f"""
                <div style="padding:10px; background-color:#ffffff; border-radius:8px; margin-bottom:10px;">
                <strong>{i+1}. {mhs.nama}</strong><br>
                NIM: {mhs.nim}<br>
                No HP: {mhs.no_hp}<br>
                Email: {mhs.email}<br>
                Alamat: {mhs.alamat}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Belum ada data.")

# ================== Tambah Data ==================
elif menu == "2":
    st.subheader("➕ Tambah Mahasiswa")
    nim = st.text_input("Masukkan NIM")
    nama = st.text_input("Masukkan Nama")
    no_hp = st.text_input("Masukkan No HP")
    email = st.text_input("Masukkan Email")
    alamat = st.text_area("Masukkan Alamat")
    if st.button("Simpan"):
        if nim and nama and no_hp and email and alamat:
            mhs = Mahasiswa(nim, nama, no_hp, email, alamat)
            st.session_state.data_mahasiswa.append(mhs)
            st.success("Data berhasil ditambahkan.")
        else:
            st.warning("Harap isi semua kolom.")

# ================== Ubah Data ==================
elif menu == "3":
    st.subheader("✏️ Ubah Mahasiswa")
    if st.session_state.data_mahasiswa:
        index = st.number_input("Masukkan nomor data yang ingin diubah:", min_value=1, max_value=len(st.session_state.data_mahasiswa))
        mhs = st.session_state.data_mahasiswa[index - 1]
        new_nim = st.text_input("Masukkan NIM baru", value=mhs.nim)
        new_nama = st.text_input("Masukkan Nama baru", value=mhs.nama)
        new_hp = st.text_input("Masukkan No HP baru", value=mhs.no_hp)
        new_email = st.text_input("Masukkan Email baru", value=mhs.email)
        new_alamat = st.text_area("Masukkan Alamat baru", value=mhs.alamat)
        if st.button("Ubah"):
            if new_nim and new_nama and new_hp and new_email and new_alamat:
                st.session_state.data_mahasiswa[index - 1] = Mahasiswa(new_nim, new_nama, new_hp, new_email, new_alamat)
                st.success("Data berhasil diubah.")
            else:
                st.warning("Harap isi semua kolom.")
    else:
        st.info("Belum ada data.")

# ================== Hapus Data ==================
elif menu == "4":
    st.subheader("🗑️ Hapus Mahasiswa")
    if st.session_state.data_mahasiswa:
        index = st.number_input("Masukkan nomor data yang ingin dihapus:", min_value=1, max_value=len(st.session_state.data_mahasiswa))
        if st.button("Hapus"):
            deleted = st.session_state.data_mahasiswa.pop(index - 1)
            st.success(f"Data {deleted.nama} berhasil dihapus.")
    else:
        st.info("Belum ada data.")

# ================== Validasi Input ==================
elif menu != "":
    st.warning("Masukkan angka 1 - 4 sesuai menu.")
