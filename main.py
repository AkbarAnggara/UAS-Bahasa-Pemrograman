from modul.daftar_nilai import ubah, hapus, cari
from view.input_nilai import tambah
from view.view_nilai import tampil, cari

while True:
    print('\nPilih salah satu menu di bawah ini:')
    print('=====================================')
    print('\n1.Tambah \n2.Tampil \n3.Hapus \n4.Ubah \n5.Cari \n6.Keluar dari program')
    x = input('\nMasukkan Pilihan Menu anda\t: ')
    if x.lower() == "1":
        tambah()
    elif x.lower() == "2":
        tampil()
    elif x.lower() == "3":
        hapus()
    elif x.lower() == "4":
        ubah()
    elif x.lower() == "5":
        cari()
    elif x.lower() == "6":
        print('\nAnda sudah keluar dari program')
        break

    else:
        print('\nPilih menu yang tersedia di atas')