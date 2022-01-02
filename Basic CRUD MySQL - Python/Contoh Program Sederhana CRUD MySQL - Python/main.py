import os
from modul import crud_mysql

run = True
while run:
    os.system('cls')
    print('=' * 10, 'TABEL MAHASISWA', '=' * 10)
    crud_mysql.show_data()
    print('=' * 37)
    print('1. Tambah Data')
    print('2. Edit Data')
    print('3. Hapus Data')
    print('4. Cari Data')
    print('0. Keluar')
    print('=' * 37)
    user_input = int(input('Pilih nomor: '))
    print('=' * 37)
    
    if user_input == 1:
        crud_mysql.tambah_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 2:
        crud_mysql.edit_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 3:
        print('Data dengan NIM yang Anda input akan dihapus!')
        crud_mysql.hapus_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 4:
        crud_mysql.cari_data()
        wait = input('\nTekan ENTER untuk kembali!\n')
    elif user_input == 0:
        run = False
    else:
        print('Pilihan tidak tersedia!')
        wait = input('\nTekan ENTER untuk kembali!\n')