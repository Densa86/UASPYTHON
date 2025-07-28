import streamlit as st

# ======= CUSTOM CSS =======
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f8;
    }
    .main {
        background-image: linear-gradient(to bottom right, #e0f7fa, #fce4ec);
        padding: 30px;
        border-radius: 10px;
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 1px solid #ccc;
        padding: 10px;
    }
    .stButton>button {
        background-color: #4Cf89;
        color: white;
        padding: 8px 16px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ====== KELAS MAHASISWA ======
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

# ====== INISIALISASI DATA ======
if 'data_mahasiswa' not in st.session_state:
    st.session_state.data_mahasiswa = []

# ====== TAMPILAN UTAMA ======
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.title("📚 Aplikasi CRUD Mahasiswa")
st.write("Kelola data mahasiswa dengan mudah dan cepat.")

menu = st.selectbox("📌 Pilih Menu", ["Lihat Data", "Tambah Data", "Ubah Data", "Hapus Data"])

# ====== MENU LIHAT DATA ======
if menu == "Lihat Data":
    st.subheader("📄 Daftar Mahasiswa")
    if st.session_state.data_mahasiswa:
        for i, mhs in enumerate(st.session_state.data_mahasiswa):
            st.markdown(f"""
                <div style="background-color:#ffffff;border:1px solid #ddd;padding:10px;border-radius:10px;margin-bottom:10px;">
                <strong>{i+1}. {mhs.nama}</strong><br>
                NIM: {mhs.nim}<br>
                No HP: {mhs.no_hp}<br>
                Email: {mhs.email}<br>
                Alamat: {mhs.alamat}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.info("Belum ada data.")

# ====== MENU TAMBAH ======
elif menu == "Tambah Data":
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
            st.success("✅ Data berhasil disimpan!")
        else:
            st.warning("⚠️ Mohon isi semua field!")

# ====== MENU UBAH ======
elif menu == "Ubah Data":
    st.subheader("✏️ Ubah Data Mahasiswa")
    if st.session_state.data_mahasiswa:
        idx = st.number_input("Pilih nomor data yang ingin diubah:", min_value=1, max_value=len(st.session_state.data_mahasiswa))
        selected = st.session_state.data_mahasiswa[idx-1]

        new_nim = st.text_input("NIM Baru", value=selected.nim)
        new_nama = st.text_input("Nama Baru", value=selected.nama)
        new_no_hp = st.text_input("No HP Baru", value=selected.no_hp)
        new_email = st.text_input("Email Baru", value=selected.email)
        new_alamat = st.text_area("Alamat Baru", value=selected.alamat)

        if st.button("Ubah"):
            selected.nim = new_nim
            selected.nama = new_nama
            selected.no_hp = new_no_hp
            selected.email = new_email
            selected.alamat = new_alamat
            st.success("✅ Data berhasil diubah!")
    else:
        st.info("Belum ada data.")

# ====== MENU HAPUS ======
elif menu == "Hapus Data":
    st.subheader("🗑️ Hapus Data Mahasiswa")
    if st.session_state.data_mahasiswa:
        idx = st.number_input("Pilih nomor data yang ingin dihapus:", min_value=1, max_value=len(st.session_state.data_mahasiswa))
        if st.button("Hapus"):
            deleted = st.session_state.data_mahasiswa.pop(idx-1)
            st.success(f"🗑️ Data {deleted.nama} berhasil dihapus!")
    else:
        st.info("Belum ada data.")

st.markdown("</div>", unsafe_allow_html=True)
