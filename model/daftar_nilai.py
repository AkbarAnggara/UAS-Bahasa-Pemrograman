data = {}


def hapus():
    print('Hapus Data Mahasiswa')
    print('====================')
    nama = input('Masukkan Nama Mahasiswa\t\t:')
    if nama in data_nilai.keys():
        del data_nilai[nama]
        print('\nData mahasiswa berhasil dihapus')
    else:
        print('\nData {0} Tidak Ditemukan'.format(nama))


def ubah():
    print('\nMengubah Data Mahasiswa')
    print('=======================')
    nama = input('Masukkan Nama Mahasiswa\t\t\t: ')
    if nama in data_nilai.keys():
        nim = int(input('Masukkan NIM Baru Mahasiswa\t\t: '))
        tugas = int(input('Masukkan Nilai Tugas Terbaru\t\t: '))
        uts = int(input('Masukkan Nilai UTS Terbaru\t\t: '))
        uas = int(input('Masukkan Nilai UAS Terbaru\t\t: '))
        hasil = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
        data_nilai[nama] = nim, tugas, uts, uas, hasil
        print('\nData mahasiswa berhasil diubah pilih nomor 2 untuk melihat data terbaru')

def cari():
        print("Cari Data Nilai Mahasiswa")