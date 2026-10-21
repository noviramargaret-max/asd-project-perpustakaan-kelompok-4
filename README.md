# Sistem Perpustakaan Mini

Project Semester Algoritma dan Struktur Data, Sistem Informasi, FTI Universitas Merdeka Malang.
Tema 3, Tahap 1 (Array & Struct).

## 1. Nama & Anggota Kelompok

**Sistem:** Sistem Perpustakaan Mini
**Kelompok:** [4]

| No | Nama | NIM | Username GitHub |
|----|------|-----|-----------------|
| 1 | [Novira Amelia Margaret] | [25083000066] | [noviramargaret@gmail.com] |
| 2 | [Diflora Hilda Jelirusma Tole] | [25083000036] | [hildatole618@gmail.com] |
| 3 | [Veronika Susanti Kae] | [25083000037] | [santiwanggul@gmail.com] |
| 4 | [Martha Hilda Eren] | [25083000055] | [hildaerend@gmail.com] |

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
| [Novira Amelia Margaret] | [F1 dan F5: Tambah Bukui Baru Dan Filter Buku Berdasarkan Genre] |
| [Diflora Hilda Jelirusma Tole] | [F2 dan F6: Tampilkan Semua Buku Dan Hapus Buku] |
| [Veronika Susanti Kae] | [F3: Cari Buku] |
| [Martha Hilda Eren] | [F4: Update Status Buku] |

## Struktur File

```
main.py   # entry point dan menu utama
buku.py   # data buku dan 6 fitur wajib Tahap 1
README.md
```
