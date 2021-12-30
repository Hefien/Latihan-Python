import pymongo


class aksesDatabase():

    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.status = True

    def login_database(self):
        try:
            # Ganti dengan link server mongodb masing-masing
            self.cluster = pymongo.MongoClient("mongodb+srv://%s:%s@cluster0.ic1ki.mongodb.net"
                                               "/myFirstDatabase?retryWrites=true&w=majority" %
                                               (self.user_id, self.password))
            self.db = self.cluster['db_kampusku']  # nama database
            self.collection = self.db['mahasiswa']  # nama koleksi
            self.cluster.server_info()
            return self.status
        except:
            self.status = False
            return self.status

    def show_data(self):
        print('-' * 40)
        print('ID  NIM\t     Nama\t\t  Prodi')
        print('-' * 40)
        display = self.collection.find({})
        for i in display:
            print(i['_id'], ' ', i['nim'], ' ',
                  i['nama'], '\t', i['prodi'])

    def get_lastID(self):
        self._id = 0
        last_id = self.collection.find({})
        for i in last_id:
            self._id = i['_id']
        return self._id + 1

    def insert_data(self, _id, nim, nama, prodi):
        upload = {"_id": _id,
                  "nim": nim, "nama": nama,
                  "prodi": prodi}
        try:
            self.collection.insert_one(upload)
            print('\tData berhasil diinput!')
        except:
            print('\tData gagal diinput!')
        print('=' * 40)
        tahan = input('\nTEKAN ENTER UNTUK KEMBALI')

    def cari_data(self, nim):
        try:
            hasil_cari = self.collection.find({'nim': nim})
            # print(hasil_cari)
            for i in hasil_cari:
                print('ID\t: ', i['_id'])
                print('NIM\t: ', i['nim'])
                print('Nama\t: ', i['nama'])
                print('Prodi\t: ', i['prodi'])
        except:
            print('\tData tidak temukan!')
        print('=' * 40)
        tahan = input('\nTEKAN ENTER UNTUK KEMBALI')

    def edit_data(self, _id, new_nim, new_nama, new_prodi):
        try:
            self.collection.update_one({'_id': _id}, {'$set':
                                                      {'nim': new_nim, 'nama': new_nama, 'prodi': new_prodi}})
            print('\tData berhasil diedit!')
        except:
            print('\tData gagal diedit!')
        print('=' * 40)
        tahan = input('\nTEKAN ENTER UNTUK KEMBALI')

    def hapus_data(self, _id):
        try:
            self.collection.delete_one({'_id': _id})
            print('\tData berhasil dihapus!')
        except:
            print('\tData gagal dihapus!')
        print('=' * 40)
        tahan = input('\nTEKAN ENTER UNTUK KEMBALI')

    def keluar(self):
        self.cluster.close()
