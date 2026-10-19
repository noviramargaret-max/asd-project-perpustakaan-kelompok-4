# Sistem Perpustakaan Mini

Project Semester Algoritma dan Struktur Data, Sistem Informasi, FTI Universitas Merdeka Malang.
Tema 3, Tahap 1 (Array & Struct).

## 1. Nama & Anggota Kelompok

**Sistem:** Sistem Perpustakaan Mini
**Kelompok:** [isi nama kelompok]

| No | Nama | NIM | Username GitHub |
|----|------|-----|-----------------|
| 1 | [nama] | [NIM] | [username] |
| 2 | [nama] | [NIM] | [username] |
| 3 | [nama] | [NIM] | [username] |

## 2. Deskripsi Sistem

Sistem Perpustakaan Mini adalah program Python berbasis terminal (CLI) untuk membantu petugas perpustakaan mengelola koleksi buku. Petugas dapat mencatat buku baru, melihat seluruh koleksi, mencari buku, memperbarui status peminjaman, memfilter berdasarkan genre, dan menghapus buku. Data disimpan dalam list of dict (Array of Struct) di memori, sehingga data hilang saat program ditutup (sesuai ketentuan Tahap 1).

## 3. Cara Menjalankan

Syarat: Python 3.8 atau lebih baru. Tidak perlu menginstal library tambahan.

```bash
git clone https://github.com/[username]/asd-project-perpustakaan-[nama-kelompok].git
cd asd-project-perpustakaan-[nama-kelompok]
python main.py
```

Pilih menu dengan mengetik angka lalu tekan Enter. Menu 7 memuat data contoh untuk demo.

## 4. Fitur yang Sudah Ada

- [x] F1: Tambah buku baru (validasi kode kosong/duplikat, field kosong, tahun terbit angka positif dan tidak melebihi tahun sekarang)
- [x] F2: Tampilkan semua buku (tabel, ringkasan total, Tersedia, Dipinjam)
- [x] F3: Cari buku (by kode: exact match, by judul: partial match tidak case sensitive)
- [x] F4: Update status buku (toggle otomatis Tersedia/Dipinjam dengan konfirmasi y/n)
- [x] F5: Filter buku berdasarkan genre (partial match, tidak case sensitive)
- [x] F6: Hapus buku (ditolak jika status Dipinjam, konfirmasi y/n sebelum hapus)

## 5. Pembagian Tugas

| Anggota | Tugas |
|---------|-------|
| [nama] | [contoh: F1 Tambah Buku + validasi] |
| [nama] | [contoh: F2 Tampilkan Semua + F3 Cari Buku] |
| [nama] | [contoh: F4 Update Status + F5 Filter Genre] |
| [nama] | [contoh: F6 Hapus Buku + README + pengujian] |

## Struktur File

```
main.py   # entry point dan menu utama
buku.py   # data buku dan 6 fitur wajib Tahap 1
README.md
```
