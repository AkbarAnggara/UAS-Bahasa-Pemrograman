from daftar_nilai import data


def tambah():
    print('\nTambah Data Nilai Mahasiswa')
    print('=============================')
    nama = input('\nMasukkan Nama Mahasiswa\t\t: ')
    nim = int(input('Masukkan NIM Mahasiswa\t\t: '))
    tugas = int(input('Masukkan Nilai Tugas Mahasiswa\t: '))
    uts = int(input('Masukkan Nilai UTS Mahasiswa\t: '))
    uas = int(input('Masukkan Nilai UAS Mahasiswa\t: '))
    hasil = (tugas*0.3) + (uts*0.35) + (uas*0.35)
    data_nilai[nama] = nim, tugas, uts, uas, hasil
    print('\nUntuk melihat data yang sudah ditambahkan silakan pilih nomor 2')