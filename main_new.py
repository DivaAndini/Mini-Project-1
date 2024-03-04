import os
os.system ('cls')
from datetime import datetime
from prettytable import PrettyTable

class CatatanKeuangan:
    def __init__(self, tanggal, jumlah, jenis_pembayaran, nama):
        self.tanggal = tanggal
        self.jumlah = jumlah
        self.nama = nama
        self.jenis_pembayaran = jenis_pembayaran
        self.next = None

class DompetDigital:
    def __init__(self):
        self.head = None

    def create_catatan_keuangan(self, tanggal, jumlah, jenis_pembayaran, nama):
        global new_node
        new_node = CatatanKeuangan(tanggal, jumlah, jenis_pembayaran, nama)
        while True:
            print('''
+--------------------------------+
| [1] Tambah Di Awal             |
| [2] Tambah Di Antara           |
| [3] Tambah Di Akhir            |
+--------------------------------+
''')
            tanya = input('Pilih tempat untuk menambahkan catatan keuangan (1/2/3): ')
            if tanya == '1':
                new_node.next = self.head
                self.head = new_node
                prev_node = None
                print(f'<< Catatan keuangan berhasil ditambahkan di awal >>')
            elif tanya == '2':
                if prev_node:
                    print("<< CATATAN SEBELUMNYA TIDAK BOLEH KOSONG >>")
                    return
                
                new_node.next = prev_node.next
                prev_node.next = new_node
                print(f'<< Catatan keuangan berhasil ditambahkan >>')
            elif tanya == '3':
                if not self.head:
                    self.head = new_node
                else:
                    current_node = self.head
                    while current_node.next:
                        current_node = current_node.next
                    current_node.next = new_node
                    print(f'<< Catatan keuangan berhasil ditambahkan di akhir >>')
            else:
                print('<< PILIHAN TIDAK VALID >>')
            break

    def read_catatan_keuangan(self):
        if not self.head:
            print("\n<< CATATAN KEUANGAN KOSONG >>")
            return
        
        current_node = self.head
        while current_node:
            new_node = current_node
            tabel = PrettyTable()
            tabel.field_names = ['Daftar Catatan Keuangan']
            tabel.align['Daftar Catatan Keuangan'] = 'l'
            tabel.add_row([f'Tanggal : {new_node.tanggal}'])
            tabel.add_row([f'Jumlah  : {new_node.jumlah}'])
            tabel.add_row([f'Jenis   : {new_node.jenis_pembayaran}'])
            tabel.add_row([f'Nama    : {new_node.nama}'])
            print(tabel)
            current_node = current_node.next

    def update_catatan_keuangan(self, nama, tanggal_baru, jumlah_baru, jenis_pembayaran_baru, nama_baru):
        if not self.head:
            print("<< CATATAN KEUANGAN KOSONG >>")
            return

        current_node = self.head
        while current_node:
            if current_node.nama == nama:
                current_node.tanggal == tanggal_baru
                current_node.jumlah == jumlah_baru
                current_node.jenis_pembayaran == jenis_pembayaran_baru
                current_node.nama == nama_baru
                current_node = current_node.next
                print(f'\n<< Catatan keuangan telah diperbarui >>')
                return
            
    def delete_catatan_keuangan(self):
        global prev_node
        prev_node = None
        while True:
            print('''
+--------------------------------+
| [1] Hapus Di Awal              |
| [2] Hapus Di Antara            |
| [3] Hapus Di Akhir             |
+--------------------------------+
''')
            pilih = input('Pilih tempat untuk menghapus catatan keuangan (1/2/3): ')
            if pilih == 1:
                if self.head is None:
                    print('<< CATATAN KEUANGAN KOSONG >>')
                    return

                current_node = self.head
                self.head = current_node.next
                print('<< CATATAN KEUANGAN BERHASIL DIHAPUS DI AWAL')
                current_node = None

            elif pilih == '2':
                if prev_node:
                    print('<< CATATAN KEUANGAN SEBELUMNYA TIDAK BOLEH KOSONG')
                    return
                
                current = prev_node.next
                if current is None:
                    print('<< CATATAN KEUANGAN SETELAHNYA TIDAK DITEMUKAN >>')

                prev_node.next = current.next
                print('<< CATATAN KEUANGAN BERHASIL DIHAPUS >>')
                current = None

            elif pilih == '3':
                if self.head is None:
                    print('<< CATATAN KEUANGAN KOSONG >>')
                    return
                
                current_node = self.head
                if current_node.next is None:
                    self.head = None
                    print(f'<< CATATAN KEUANGAN BERHASIL DIHAPUS DI AKHIR >>')
                    return

                while current_node.next.next:
                    current_node = current_node.next

                last_node = current_node.next
                current_node.next = None
                print(f'<< CATATAN KEUANGAN BERHASIL DIHAPUS DI AKHIR >>')
                last_node = None

        
dompet = DompetDigital()

        
def create_catke():
    print('''\n
+--------------------------------+
|     Buat Catatan Keuangan      |
+--------------------------------+''')
    while True:
        try:
            tanggal = input('Masukkan tanggal (DD/MM/YYYY): ')
            datetime.strptime(tanggal, "%d/%m/%Y")
            break
        except ValueError:
            print('<< INPUT TANGGAL TIDAK SESUAI >>')

    while True:
        try:
            jumlah = int(input('Masukkan jumlah: Rp '))
            if jumlah <= 0:
                print('<< Masukkan jumlah uang yang sesuai >>')
            else:
                break
        except ValueError:
            print('<< INPUT TIDAK VALID >>')
        break

    while True:
        jenis_pembayaran = input('Masukkan jenis pembayaran (tunai/non tunai): ').title()
        break

    while True:
        nama = input('Masukkan nama catatan keuangan: ').title()
        if not nama.isalpha():
            print('<< Input nama tidak sesuai >>')
        break

    print('\n<< CATATAN KEUANGAN BERHASIL DIBUAT >>' )
    dompet.create_catatan_keuangan(tanggal, jumlah, jenis_pembayaran, nama)

def read_catke():
    dompet.read_catatan_keuangan()        

def update_catke():
    read_catke()
    while True:
        nama = input('Masukkan nama catatan keuangan yang ingin diperbarui: ')
        if not nama.isalpha():
            print('<< Input nama tidak sesuai >>')      
            continue
        
        print('''
+--------------------------------+
|    PERBARUI CATATAN KEUANGAN   |
+--------------------------------+''')
        while True:
            try:
                tanggal_baru = input('Masukkan tanggal yang terbaru: ')
                datetime.strptime(tanggal_baru, "%d/%m/%Y")
            except ValueError:
                print('<< INPUT TANGGAL TIDAK SESUAI >>')
            break

        jumlah_baru = int(input('\nMasukkan jumlah: Rp '))
        jenis_pembayaran_baru = input('\nMasukkan jenis pembayaran terbaru (tunai/non tunai): ').title
        nama_baru = input('\nMasukkan nama yang terbaru: ').title
        dompet.update_catatan_keuangan(nama, tanggal_baru, jumlah_baru, jenis_pembayaran_baru, nama_baru)
        break

def delete_catke():
        print('''
+--------------------------------+
|     HAPUS CATATAN KEUANGAN     |
+--------------------------------+''')
        read_catke
        dompet.delete_catatan_keuangan(prev_node)
        
while True:
    print('''
+--------------------------------+
|        Catatan Keuangan        |
+--------------------------------+
| [1] Buat Catatan Keuangan      |
| [2] Lihat Catatan Keuangan     |
| [3] Perbarui Catatan Keuangan  |
| [4] Hapus Catatan Keuangan     |
| [5] Keluar dari Program        |
+--------------------------------+''')
    pilihan = input('Masukkan pilihan (1/2/3/4): ')
    if pilihan == '1':
        create_catke()
    elif pilihan == '2':
        read_catke()
    elif pilihan == '3':
        update_catke()
    elif pilihan == '4':
        delete_catke()
    elif pilihan == '5':
        print('\n<< PROGRAM DOMPET DIGITAL SELESAI >>')
        break