import pymysql

# Membuka koneksi ke database
"""
Ganti nama-nama berikut dengan punya masing-masing:
db_mahasiswa -> ini nama database
mahasiswa -> nama tabel
nim, nama, kode_prodi -> nama head kolom
"""
db = pymysql.connect(host='localhost', user='root',
                     password='', database='db_mahasiswa')
# Menyiapkan objek cursor menggunakan method cursor()
cursor = db.cursor()

# # Start - Untuk cek terhubung atau tidak
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print ("Database version : %s " % data)
# # End - cek terhubung

# # Start - Membuat table ke database
# buat_table = """create table mahasiswa (
#         nim varchar(15) not null,
#         nama varchar(50) not null,
#         kode_prodi char(2) not null,
#         primary key (nim)
#         )"""
# cursor.execute(buat_table)
# print('Table berhasil dibuat!')
# # End - membuat table

# # Start - Menambah data ke dalam tabel
# sql = """insert into mahasiswa(
#     nim, nama, kode_prodi)
#     values('1220001', 'Suhaefi Fauzian', 'IF')"""

# nim = '03122021'
# nama = 'Sterys Himari'
# kode_prodi = 'SF'
# # End - Menambah data

# #  Start - menambahkan data secara dinamis
# sql = "insert into mahasiswa( \
#     nim, nama, kode_prodi) \
#     values('%s','%s', '%s')" % \
#     (nim, nama, kode_prodi)
# try:
#     # menjalankan command SQL
#     cursor.execute(sql)
#     # buat perubahan pada database
#     db.commit()
#     # Pemberitahuan
#     print('Data berhasil di inputkan!')
# except:
#     # rollback jika terdapat error
#     db.rollback()
# # End - Menambah data secara dinamis

# # Start - membaca satu data dalam tabel database
# sql = "select * from mahasiswa \
#     where nim = '%s'" % ('03122021')

# # membaca semua data dalam tabel
# sql = "select * from mahasiswa"

# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     # print(results)
#     for row in results:
#         nim = row[0]
#         nama = row[1]
#         kode_prodi = row[2]

#         print(f'NIM\t= {nim}\nNama\t= {nama}\nProdi\t= {kode_prodi}\n')

# except:
#     print('Error!')
# # End - membaca data

# # Start - Update / edit data
# sql = "UPDATE mahasiswa SET nama = %s,\
#     kode_prodi = %s WHERE nim = %s"
# val = ("Yukino Yuuki", "IF", "03122021")

# try:
#     cursor.execute(sql, val)
#     db.commit()
#     print("{} data diubah".format(cursor.rowcount))
# except:
#     db.rollback()
# # End - Update data

# # Start - Hapus data
# sql = "delete from mahasiswa where nim = %s" % ("3220001")

# try:
#     cursor.execute(sql)
#     db.commit()
#     print('{} data dihapus'.format(cursor.rowcount))
# except:
#     db.rollback()
# # End - Hapus data

# disconnect from server
db.close()
