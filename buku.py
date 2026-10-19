"""
buku.py - Modul data buku (Tahap 1: Array & Struct)

Satu buku = dict (struct), seluruh koleksi = list (array of struct).
Atribut wajib: kode_buku, judul, pengarang, genre, tahun_terbit, status.
"""

from datetime import datetime

STATUS_TERSEDIA = "Tersedia"
STATUS_DIPINJAM = "Dipinjam"


# ---------------------------------------------------------------------------
# Fungsi bantu (helper)
# ---------------------------------------------------------------------------

def minta_input(pesan):
    """Minta input dari petugas dan buang spasi di awal/akhir."""
    return input(pesan).strip()


def minta_konfirmasi(pesan):
    """Ulangi sampai petugas mengetik y atau n. Mengembalikan True jika y."""
    while True:
        jawab = minta_input(pesan + " (y/n): ").lower()
        if jawab == "y":
            return True
        if jawab == "n":
            return False
        print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")


def penanda_status(status):
    """Ubah status menjadi penanda visual: [TERSEDIA] atau [DIPINJAM]."""
    return "[" + status.upper() + "]"


def cari_berdasarkan_kode(koleksi, kode):
    """Cari 1 buku dengan kode persis sama. Mengembalikan dict atau None."""
    for buku in koleksi:
        if buku["kode_buku"] == kode:
            return buku
    return None


def kode_sudah_ada(koleksi, kode):
    """Cek duplikat kode (tidak membedakan huruf besar/kecil)."""
    for buku in koleksi:
        if buku["kode_buku"].lower() == kode.lower():
            return True
    return False


def tampilkan_tabel(daftar_buku):
    """Cetak daftar buku dalam bentuk tabel dengan lebar kolom otomatis."""
    kolom = ["No", "Kode", "Judul", "Pengarang", "Genre", "Tahun Terbit", "Status"]

    # Susun isi baris dulu, supaya lebar kolom bisa dihitung dari data
    baris = []
    for nomor, buku in enumerate(daftar_buku, start=1):
        baris.append([
            str(nomor),
            buku["kode_buku"],
            buku["judul"],
            buku["pengarang"],
            buku["genre"],
            str(buku["tahun_terbit"]),
            penanda_status(buku["status"]),
        ])

    lebar = [len(nama) for nama in kolom]
    for isi in baris:
        for i, sel in enumerate(isi):
            lebar[i] = max(lebar[i], len(sel))

    def format_baris(isi):
        return " | ".join(sel.ljust(lebar[i]) for i, sel in enumerate(isi))

    garis = "-+-".join("-" * w for w in lebar)
    print(format_baris(kolom))
    print(garis)
    for isi in baris:
        print(format_baris(isi))
    print(garis)


def tampilkan_detail(buku):
    """Cetak seluruh atribut satu buku."""
    print(f"  Kode Buku    : {buku['kode_buku']}")
    print(f"  Judul        : {buku['judul']}")
    print(f"  Pengarang    : {buku['pengarang']}")
    print(f"  Genre        : {buku['genre']}")
    print(f"  Tahun Terbit : {buku['tahun_terbit']}")
    print(f"  Status       : {penanda_status(buku['status'])}")


# ---------------------------------------------------------------------------
# Fitur 1: Tambah Buku Baru
# ---------------------------------------------------------------------------

def tambah_buku(koleksi):
    print("\n=== TAMBAH BUKU BARU ===")

    kode = minta_input("Kode buku    : ")
    if kode == "":
        print("Gagal: kode buku tidak boleh kosong.")
        return
    if kode_sudah_ada(koleksi, kode):
        print(f"Gagal: kode buku '{kode}' sudah digunakan. Kode harus unik.")
        return

    judul = minta_input("Judul        : ")
    if judul == "":
        print("Gagal: judul tidak boleh kosong.")
        return

    pengarang = minta_input("Pengarang    : ")
    if pengarang == "":
        print("Gagal: pengarang tidak boleh kosong.")
        return

    genre = minta_input("Genre        : ")
    if genre == "":
        print("Gagal: genre tidak boleh kosong.")
        return

    tahun_teks = minta_input("Tahun terbit : ")
    if tahun_teks == "":
        print("Gagal: tahun terbit tidak boleh kosong.")
        return
    try:
        tahun = int(tahun_teks)
    except ValueError:
        print("Gagal: tahun terbit harus berupa angka bulat.")
        return
    if tahun <= 0:
        print("Gagal: tahun terbit harus berupa angka bulat positif.")
        return
    if tahun > datetime.now().year:
        print(f"Gagal: tahun terbit tidak boleh lebih besar dari tahun sekarang ({datetime.now().year}).")
        return

    buku_baru = {
        "kode_buku": kode,
        "judul": judul,
        "pengarang": pengarang,
        "genre": genre,
        "tahun_terbit": tahun,
        "status": STATUS_TERSEDIA,  # status awal otomatis
    }
    koleksi.append(buku_baru)
    print(f"Buku '{judul}' dengan kode {kode} berhasil ditambahkan ke koleksi.")


# ---------------------------------------------------------------------------
# Fitur 2: Tampilkan Semua Buku
# ---------------------------------------------------------------------------

def tampilkan_semua_buku(koleksi):
    print("\n=== DAFTAR SEMUA BUKU ===")
    if len(koleksi) == 0:
        print("Belum ada buku dalam koleksi.")
        return

    tampilkan_tabel(koleksi)

    jumlah_tersedia = 0
    jumlah_dipinjam = 0
    for buku in koleksi:
        if buku["status"] == STATUS_TERSEDIA:
            jumlah_tersedia += 1
        else:
            jumlah_dipinjam += 1

    print(f"Total buku: {len(koleksi)} | Tersedia: {jumlah_tersedia} | Dipinjam: {jumlah_dipinjam}")


# ---------------------------------------------------------------------------
# Fitur 3: Cari Buku
# ---------------------------------------------------------------------------

def cari_buku(koleksi):
    print("\n=== CARI BUKU ===")
    print("1. Cari berdasarkan kode (harus persis sama)")
    print("2. Cari berdasarkan judul (sebagian kata, tidak case sensitive)")
    mode = minta_input("Pilih mode (1/2): ")

    if mode not in ("1", "2"):
        print("Pilihan tidak valid. Masukkan 1 atau 2.")
        return

    kata_kunci = minta_input("Kata kunci: ")
    if kata_kunci == "":
        print("Gagal: kata kunci tidak boleh kosong.")
        return

    if mode == "1":
        buku = cari_berdasarkan_kode(koleksi, kata_kunci)
        if buku is None:
            print(f"Buku dengan kode '{kata_kunci}' tidak ditemukan dalam koleksi.")
            return
        print("Ditemukan 1 buku:")
        tampilkan_detail(buku)
    else:
        hasil = [b for b in koleksi if kata_kunci.lower() in b["judul"].lower()]
        if len(hasil) == 0:
            print(f"Buku dengan judul '{kata_kunci}' tidak ditemukan dalam koleksi.")
            return
        print(f"Ditemukan {len(hasil)} buku dengan judul mengandung '{kata_kunci}':")
        tampilkan_tabel(hasil)


# ---------------------------------------------------------------------------
# Fitur 4: Update Status Buku
# ---------------------------------------------------------------------------

def update_status_buku(koleksi):
    print("\n=== UPDATE STATUS BUKU ===")
    kode = minta_input("Kode buku: ")
    if kode == "":
        print("Gagal: kode buku tidak boleh kosong.")
        return

    buku = cari_berdasarkan_kode(koleksi, kode)
    if buku is None:
        print(f"Buku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return

    print("Informasi buku:")
    print(f"  Judul     : {buku['judul']}")
    print(f"  Pengarang : {buku['pengarang']}")
    print(f"  Status    : {penanda_status(buku['status'])}")

    # Arah perubahan ditentukan otomatis dari status saat ini
    if buku["status"] == STATUS_TERSEDIA:
        status_baru = STATUS_DIPINJAM
        kata_kerja = "dipinjam"
    else:
        status_baru = STATUS_TERSEDIA
        kata_kerja = "dikembalikan"

    if not minta_konfirmasi(f"Ubah status menjadi {status_baru}?"):
        print("Perubahan status dibatalkan.")
        return

    status_lama = buku["status"]
    buku["status"] = status_baru
    print(f"Buku '{buku['judul']}' berhasil {kata_kerja}. "
          f"Status diubah: {status_lama} menjadi {status_baru}.")


# ---------------------------------------------------------------------------
# Fitur 5: Filter Buku Berdasarkan Genre
# ---------------------------------------------------------------------------

def filter_berdasarkan_genre(koleksi):
    print("\n=== FILTER BUKU BERDASARKAN GENRE ===")
    genre = minta_input("Masukkan genre: ")
    if genre == "":
        print("Gagal: genre tidak boleh kosong.")
        return

    hasil = [b for b in koleksi if genre.lower() in b["genre"].lower()]
    if len(hasil) == 0:
        print(f"Tidak ada buku dengan genre '{genre}' dalam koleksi.")
        return

    print(f"Menampilkan buku genre: {genre} ({len(hasil)} buku ditemukan).")
    tampilkan_tabel(hasil)


# ---------------------------------------------------------------------------
# Fitur 6: Hapus Buku
# ---------------------------------------------------------------------------

def hapus_buku(koleksi):
    print("\n=== HAPUS BUKU ===")
    kode = minta_input("Kode buku: ")
    if kode == "":
        print("Gagal: kode buku tidak boleh kosong.")
        return

    buku = cari_berdasarkan_kode(koleksi, kode)
    if buku is None:
        print(f"Buku dengan kode '{kode}' tidak ditemukan dalam koleksi.")
        return

    # Cek status SEBELUM meminta konfirmasi
    if buku["status"] == STATUS_DIPINJAM:
        print(f"Buku '{buku['judul']}' tidak dapat dihapus karena sedang dalam status Dipinjam. "
              "Pastikan buku dikembalikan terlebih dahulu sebelum dihapus dari koleksi.")
        return

    print("Detail buku yang akan dihapus:")
    print(f"  Judul     : {buku['judul']}")
    print(f"  Pengarang : {buku['pengarang']}")
    print(f"  Genre     : {buku['genre']}")
    print(f"  Status    : {penanda_status(buku['status'])}")

    if minta_konfirmasi("Yakin ingin menghapus buku ini?"):
        koleksi.remove(buku)
        print(f"Buku '{buku['judul']}' dengan kode {buku['kode_buku']} berhasil dihapus dari koleksi.")
    else:
        print("Penghapusan dibatalkan.")


# ---------------------------------------------------------------------------
# Tambahan: data contoh untuk demo/pengujian (data hilang saat program ditutup)
# ---------------------------------------------------------------------------

def muat_data_contoh(koleksi):
    contoh = [
        ("BK001", "Algoritma dan Pemrograman", "Rinaldi Munir", "Teknologi", 2020),
        ("BK002", "Pengantar Algoritma", "Thomas Cormen", "Teknologi", 2009),
        ("BK003", "Laskar Pelangi", "Andrea Hirata", "Fiksi", 2005),
        ("BK004", "Bumi Manusia", "Pramoedya Ananta Toer", "Fiksi Sejarah", 1980),
        ("BK005", "Kosmos", "Carl Sagan", "Sains", 1980),
    ]
    ditambah = 0
    for kode, judul, pengarang, genre, tahun in contoh:
        if not kode_sudah_ada(koleksi, kode):
            koleksi.append({
                "kode_buku": kode,
                "judul": judul,
                "pengarang": pengarang,
                "genre": genre,
                "tahun_terbit": tahun,
                "status": STATUS_TERSEDIA,
            })
            ditambah += 1
    print(f"{ditambah} data contoh dimuat ke koleksi.")
