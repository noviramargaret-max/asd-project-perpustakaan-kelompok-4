"""
main.py - Entry point Sistem Perpustakaan Mini (Tahap 1)
Jalankan dengan: python main.py
"""

import buku


def tampilkan_menu():
    print("\n==============================")
    print("   SISTEM PERPUSTAKAAN MINI")
    print("==============================")
    print("1. Tambah buku baru")
    print("2. Tampilkan semua buku")
    print("3. Cari buku")
    print("4. Update status buku (pinjam/kembali)")
    print("5. Filter buku berdasarkan genre")
    print("6. Hapus buku")
    print("7. Muat data contoh (untuk demo)")
    print("0. Keluar")


def main():
    # Array of Struct: list berisi dict, satu dict = satu buku
    koleksi_buku = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            buku.tambah_buku(koleksi_buku)
        elif pilihan == "2":
            buku.tampilkan_semua_buku(koleksi_buku)
        elif pilihan == "3":
            buku.cari_buku(koleksi_buku)
        elif pilihan == "4":
            buku.update_status_buku(koleksi_buku)
        elif pilihan == "5":
            buku.filter_berdasarkan_genre(koleksi_buku)
        elif pilihan == "6":
            buku.hapus_buku(koleksi_buku)
        elif pilihan == "7":
            buku.muat_data_contoh(koleksi_buku)
        elif pilihan == "0":
            print("Terima kasih. Data tidak disimpan permanen pada Tahap 1.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 7.")


if __name__ == "__main__":
    main()
