import pymongo

"""
Untuk perintah CRUD yang ada di sini, karena ini basic
maka jalankan satu persatu. Misal setelah berhasil menambah data,
kemudian berikutnya ingin menampilkan data maka hapus atau jadikan komentar
terlebih dahulu perintah tambah datanya. Intinya lakukan satu-persatu.
"""

# # Konek ke server
client_server = pymongo.MongoClient("link server mongodb disimpan disini")
# # cek koneksi terhubung ke server
# try:
#     info = client_server.server_info()
#     print(info)
# except:
#     print('Gagal terhubung')

# # Membuat database
# try:
#     db = client_server["db_kampusku"]
#     collection = db["mahasiswa"]
# #     print('Database berhasil dibuat!')
# except:
#     print('Database gagal dibuat!')

# # Konek ke collection pada database


# # Tambah data
# # {"key": value}
post_1 = {"_id": 1, "nim": "1230021",
          "nama": "Udin",
          "kode_prodi": "IF"}

post_2 = {"_id": 2, "nim": "1230022",
          "nama": "Jamal",
          "kode_prodi": "IF"}

post_3 = {"_id": 3, "nim": "1220999",
          "nama": "Unknown",
          "kode_prodi": "IF"}

# try:
#     # Tambah satu data
#     collection.insert_one(post_2)
#     # Tambah beberapa data
#     # collection.insert_many([post_2, post_3])
#     print('Data sukses diinput!')
# except:
#     print('gagal!')

# # Mencari data
# hasil = collection.find({"nama": "Udin"})

# for cari in hasil:
#     print('NIM\t: ', cari["nim"])
#     print('Nama\t: ', cari["nama"])
#     print('Prodi\t: ', cari["kode_prodi"])

# # Atau
# hasil = collection.find_one({"_id":1})
# print(hasil)

# # Menampilkan semua data dengan find()
# hasil = collection.find({})
# for i in hasil:
#     print('NIM\t: ', i["nim"])
#     print('Nama\t: ', i["nama"])
#     print('Prodi\t: ', i["kode_prodi"])
#     print()

# # Update data
# update_data = collection.update_one({"_id":1}, {"$set":{"nim": "1220999", "kode_prodi": "IF", "nama":"Unknown"}})

# # Menghapus data
# hapus_data = collection.delete_one({"_id":2})


# # Menambah field / key
# update_data = collection.update_one({"_id":2}, {"$set":{"status": "aktif"}})

# # Menghitung banyaknya data
# banyak_data = collection.count_documents({})
# print('Banyak data: ', banyak_data)
