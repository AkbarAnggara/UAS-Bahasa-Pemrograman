# UAS Bahasa Pemrograman Semester 1

Nama : Bangkit Akbar Anggara<br>
NIM : 312010148<br>
Kelas : TI.20.B.1<br>

# Soal
Berikut ini adalah soal Ujian Akhir Semester(UAS) 1 yang diberikan oleh dosen saya<br>
![soal.png](Pic/soal.png)<br>
Disitu tertulis kita disuruh membuat package dan modul lalu jelaskan di github berserta gambar screen shotnya<br>

# Penyelesaian
Oke Berikut adalah syntax - syntax yang saya gunakan untuk mengerjakan soal diatas<br>
1. Package modul(daftar_nilai) [Click Here](model/daftar_nilai.py)
2. Package view(input_nilai) [Click Here](view/input_nilai.py) dan view(view_nilai) [Click Here](view/view_nilai.py)
3. modul main [Click Here](main.py)

Setelah kalian melihat syntax diatas saya akan menjelaskannya satu - persatu:<br>
1. Daftar_Nilai<br>
  - Dictionary<br>
![dictionary.png](Pic/dictionary.png)<br>
Penjelasan:<br>
    - Disini kita menggunakan dictionary ya untuk menyimpan inputan data mahasiswa<br>
  
  - Def tambahkan<br>
![tambahkan.png](Pic/tambahkan.png)<br>
Penjelasan:<br>
    - Dibagian ini kita gunakan print untuk penulisan bagian input data mahasiswa nanti agar terlihat rapih<br>
  
  - Def hapus<br>
![hapus.png](Pic/hapus.png)<br>
Penjelasan:<br>
    - Disini kita buat inputan yang menginput nama<br>
    - Gunanya untuk menghapus data mahasiswa dari nama mahasiswa itu sendiri<br>
    - Kita gunakan del untuk fungsi menghapus datanya<br>
    - (If)Jika mahasiswa tersebut ada maka data mahasiswa tersebut akan terhapus<br>
    - (Else)Jika nama mahasiswa tersebut tidak ada maka datanya tidak akan ditemukan<br>
  
  - Def ubah<br>
![ubah.png](Pic/ubah.png)<br>
Penjelasan:<br>
    - Disini kita hampir sama dengan yang hapus, kita gunakan inputan nama untuk mengubah NIM, Nilai Tugas, Ujian Tengah Semester(UTS), ataupun Ujian Akhir Semester(UAS)<br>
    - Lalu setelah kita memasukkan nama maka dictionary akan mengeksekusi program menggunakan keys untuk mencari data dari nama mahasiswa tersebut<br>
    - (If)Jika nama mahasiswa tersebut ketemu atau ada didalam data maka program akan masuk ke inputan NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS yang baru<br>
    - (Else)Jika nama mahasiswa tersebut tidak ada didalam data maka program akan memunculkan tulisan atau perintah bahwa data mahasiswa tidak ada<br>

  - Def cari<br>
![cari.png](Pic/cari.png)<br>
Penjelasan:<br>
    - Fungsinya sama dengan tambahkan<br>
 
2. Input_Nilai<br>
  - From dan import<br>
![from.png](Pic/from.png)<br>
Penjelasan:<br>
    - From digunakan untuk memanggil package sementara import untuk tujuan yang kita pilih yaitu modul daftar_nilai<br>
    - Lalu kita gunakan import data_mahasiswa itu gunanya agar saat kita menginputkan data atau setiap kali kita menambah data maka data mahasiswa secara otomatis akan masuk kedalam dictionary meskipun beda atau terpisah package dan juga modulnya<br>

  - Def tambah data<br>
![tambah_data.png](Pic/tambah_data.png)<br>
Penjelasan:<br>
    - Disini kita buat inputan karena tadi kita sudah membuat kata - kata outputnya kali ini kita cukup membuat inputan data mahasiswanya saja<br>
    - Jangan lupa gunakan perkalian untuk menghitunghasil total atau rata- ratanya<br>

3. View_Nilai<br>
  - From dan import<br>
![from.png](Pic/from.png)<br>
Penjelasan:<br>
    - Fungsinya sama saja dengan yang ada dibagian Input_Nilai<br>
 
  - Def tampil<br>
![tampil.png](Pic/tampil.png)<br>
Penjelasan:<br>
    - Disini kita buat sebuah tabel untuk menampilkan data - data dan nama - nama mahasiswa didalam dictionary<br>
    - (If)Jika terdapat data maka data dan nama mahasiswa tersebut akan muncul<br>
    - Disini kita menggunakan for untuk melakukan perulangan nomor urut<br>
    - (Else)Jika kita belum menginputkan data sama sekali maka akan muncul tulisan "tidak ada data"<br>
    
  - Def cari data<br>
![cari_data.png](Pic/cari_data.png)<br>
Penjelasan:<br>
    - Tadi kita sudah buat print sama seperti dibagian Input_Nilai<br>
    - Kita akan langsung membuat inputan dengan format nama untuk mencari data dari mahasiswa yang sedang kita cari<br>
    - (If)Jika data mahasiswa yang dicari ada didalam dictionary maka data baik Nama, NIM, Nilai Tugas, Nilai UTS, dan Nilai UAS akan muncul<br>
    - (Else)Jika data mahasiswa yang dicari tidak ada didalam dictionary maka akan muncul tulisan "datanya tidak ada"<br>
 
4. Main<br>
  - From dan import<br>
![memanggil_modul.png](Pic/memanggil_modul.png)<br>
Penjelasan:<br>
    - Sama seperti sebelumnya hanya saja disini sedikit berbeda<br>
    - From disini kita tulis package.modulnya lalu import fungsi(def) tadi<br>
    - Karena dibagian main ini kita akan menggunakan atau membuat syntax pilihan menu<br>
   
  - While True<br>
![pilih_menu.png](Pic/pilih_menu.png)<br>
Penjelasan:<br>
    - Kita gunakan print untuk membuat pilihan menunya<br>
    - Lalu kita buat inputan untuk memilih menu nanti ketika program dijalankan<br>
    - (If dan Elif)Kita gunakan karena kita akan membuat cabang pilihan yang banyak<br>
    - Lalu dibawahnya kita tambahkan  juga fungsi - fungsi yang sudah kita buat tadi<br>
    - Pada perintah ke 6 kita gunakan break untuk keluar dari program yang kita jalankan<br>
    - (Else)Jika kita tidak memilih salah satu menu tersebut maka akan muncul peringatan "pilih menu yang tersedia diatas"<br>
    
Setelah semmuanya selesai maka kita akan menjalankan/run syntax untuk mengerun atau menjalankan syntax harus yang main karena pilihan menunya ada di main
Berikut adalah tampilan dari program atau syntax- syntax yang sudah kita buat tadi<br>

1. Tambah data mahasiswa<br>
![tambah_akbar.png](Pic/tambah_akbar.png)<br>
![tambah_qiqi.png](Pic/tambah_qiqi.png)<br>

2. Tampilkan data mahasiswa<br>
Jika kita sudah memasukkan atau menginputkan data mahasiswa<br>
![tampilkan_data.png](Pic/tampilkan_data.png)<br>
Jika kita belum menginputkan data mahasiswa<br>
![tidak_ada_data.png](Pic/tidak_ada_data.png)<br>

3. Menghapus data mahasiswa<br>
Jika kita sudah memasukkan atau menginputkan data mahasiswa<br>
!hapus_data_qiqi.png](Pic/hapus_data_qiqi.png)<br>
Jika kita belum menginputkan data mahasiswa<br>
![pencarian_tidak_ada.png](Pic/pencarian_tidak_ada.png)<br>
Tampilan data jika kita sudah berhasil menghapus data mahasiswa<br>
![tampilkan_data_setelah_dihapus.png](Pic/tampilkan_data_setelah_dihapus.png)

4. Mengubah data mahasiswa<br>
Jika kita sudah memasukkan atau menginputkan data mahasiswa<br>
![ubah_data.png](Pic/ubah_data.png)<br>
Jika kita belum menginputkan data mahasiswa<br>
![tidak_ada_data_dirubah.png](Pic/tidak_ada_data_dirubah.png)<br>
Tampilan data jika kita sudah berhasil mengubah data mahasiswa<br>
![tampilkan_data_setelah_diubah.png](Pic/tampilkan_data_setelah_diubah.png)

5. Mencari data mahasiswa<br>
Jika kita sudah memasukkan atau menginputkan data mahasiswa<br>
![mencari_data_qiqi.png](Pic/mencari_data_qiqi.png)<br>
Jika kita belum menginputkan data mahasiswa<br>
![data_tidak_bisa_dicari.png](Pic/data_tidak_bisa_dicari.png)<br>

6. Kelar dari program<br>
![keluar_dari_program.png](Pic/keluar_dari_program.png)<br>

7. Pilih menu yang tersedia diatas<br>
![pili_menu_tersedia.png](Pic/pilih_menu_tersedia.png)

Oke sekian penjelasan dan selesai sudah tugas Ujian Akhir Semester(UAS) 1 untuk Mata Kuliah Bahasa Pemrograman<br>
Sekian Terimakasih Banyak<br>

||==== Bangkit Akbar Anggara ====||
||==== TI.20.B.1 ====||
||==== 312010148 ====||
