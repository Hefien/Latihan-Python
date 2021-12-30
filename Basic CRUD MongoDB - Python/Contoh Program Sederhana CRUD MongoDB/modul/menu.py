import os
from modul import database

# Menu utama untuk akses database


def menu_utama(akun):

    status = True
    while status:
        os.system('cls')
        _id = akun.get_lastID()
        akun.show_data()
        print('=' * 40)
        print('   CRUD DATABASE MONGODB by: 1220001')
        print('=' * 40)
        print('1. INPUT DATA')
        print('2. CARI DATA')
        print('3. EDIT DATA')
        print('4. DELETE DATA')
        print('0. KELUAR')
        print('=' * 40)
        pilihan = input('Pilih Nomor: ')
        print('=' * 40)

        if pilihan == '1':
            print('Nomor\t: ', _id)
            nim = input('NIM\t: ')
            nama = input('Nama\t: ')
            kode_prodi = input('Prodi\t: ')
            print('=' * 40)
            akun.insert_data(_id, nim, nama, kode_prodi)
        elif pilihan == '2':
            user_input = input('Masukkan NIM: ')
            print('=' * 40)
            hasil = akun.cari_data(user_input)
            print(hasil)
        elif pilihan == '3':
            _id = int(input('Masukkan ID: '))
            nim = input('NIM baru\t: ')
            nama = input('Nama baru\t: ')
            kode_prodi = input('Prodi baru\t: ')
            print('=' * 40)
            akun.edit_data(_id, nim, nama, kode_prodi)
        elif pilihan == '4':
            _id = int(input('Hapus data dengan ID: '))
            print('=' * 40)
            akun.hapus_data(_id)
        elif pilihan == '0':
            akun.keluar()
            status = False
            print('=' * 40)
            print('\tAnda telah keluar program!')
            print('=' * 40)
        else:
            print('=' * 40)
            print('\tPilihan tidak tersedia!')
            print('=' * 40)
            tahan = input('\nTEKAN ENTER UNTUK KEMBALI')

# Form untuk login


def _login():
    status = True
    while status:
        os.system('cls')
        print('=' * 30)
        print('LOGIN KE DATABASE DBLATIHAN')
        print('=' * 30)
        user_id = input('ID\t\t: ')
        password = input('Password\t: ')
        print('=' * 30)

        akun_login = database.aksesDatabase(user_id, password)
        cek_login = akun_login.login_database()
        if cek_login == True:
            menu_utama(akun_login)
            status = False
