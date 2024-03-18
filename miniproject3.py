import os
os.system ('cls')
from datetime import datetime
from prettytable import PrettyTable 

class Node:
    def __init__(self, nama, tanggal, jumlah, jenis_pembayaran):
        self.nama = nama
        self.tanggal = tanggal
        self.jumlah = jumlah
        self.jenis_pembayaran = jenis_pembayaran
        self.next = None
        self.prev = None

class DompetDigital:
    def __init__(self):
        self.head = None

    def create_catatan_keuangan(self, nama, tanggal, jumlah, jenis_pembayaran):
        catatan = Node(nama, tanggal, jumlah, jenis_pembayaran)
        while True:
            print('''
+--------------------------------+
|             Tempat             |
+--------------------------------+
| [1] Sisipkan dari Depan        |
| [2] Sisipkan Setelah ...       |
| [3] Sisipkan dari Belakang     |
+--------------------------------+''')
            tanya = input('Pilih tempat untuk menambahkan catatan keuangan (1/2/3): ')
            if tanya == '1':
                if self.head is None:
                    new_node = catatan
                    self.head = new_node
                    print('\n<< CATATAN KEUANGAN BERHASIL DITAMBAHKAN DARI DEPAN >>')
                    return
                new_node = catatan
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                print('\n<< CATATAN KEUANGAN BERHASIL DITAMBAHKAN DARI DEPAN >>')

            elif tanya == '2':
                self.read_catatan_keuangan()
                nama = input('Tambahkan catatan keuangan setelah (masukkan nama): ').title()
                if self.head is None:
                    print("\n<< CATATAN KEUANGAN KOSONG >>")
                    return
                else:
                    n = self.head
                    while n is not None:
                        if n.nama == nama:
                            break
                        n = n.next
                    if n is None:
                        print(f'<< {n.nama} TIDAK TERDAPAT DALAM DAFTAR >>')
                    else:
                        new_node = catatan
                        new_node.prev = n
                        new_node.next = n.next
                        if n.next is not None:
                            n.next.prev = new_node
                        n.next = new_node
                        print(f'<< CATATAN KEUANGAN BERHASIL DISISIPKAN SETELAH {n.nama} >>')
                        return

            elif tanya == '3':
                if self.head is None:
                    new_node = catatan
                    self.head = new_node
                    print('<< CATATAN KEUANGAN BERHASIL DISISIPKAN DARI BELAKANG >>')
                    return
                now = self.head
                while now.next is not None:
                    now = now.next
                new_node = catatan
                now.next = new_node
                new_node.prev = now
                print('<< CATATAN KEUANGAN BERHASIL DISISIPKAN DARI BELAKANG >>')
            else:
                print('<< PILIHAN TIDAK VALID >>')
            break

    def read_catatan_keuangan(self):
        if not self.head:
            print("\n<< CATATAN KEUANGAN KOSONG >>")
            return
        
        current_node = self.head
        tabel = PrettyTable()
        tabel.field_names = ['Daftar Catatan Keuangan']
        tabel.align['Daftar Catatan Keuangan'] = 'l'
        while current_node:
            tabel.add_row([f'Nama    : {current_node.nama}'])
            tabel.add_row([f'Tanggal : {current_node.tanggal}'])
            tabel.add_row([f'Jumlah  : Rp {current_node.jumlah}'])
            tabel.add_row([f'Jenis   : {current_node.jenis_pembayaran}\n'])
            current_node = current_node.next
        print(tabel)

    def update_catatan_keuangan(self, nama_lama, tanggal_baru, jumlah_baru, jenis_pembayaran_baru, nama_baru):
        if self.head is None:
            print("<< CATATAN KEUANGAN KOSONG >>")
            return
        
        current = self.head
        while current:
            if current.nama == nama_lama:
                current.tanggal = tanggal_baru
                current.jumlah = jumlah_baru
                current.jenis_pembayaran = jenis_pembayaran_baru
                current.nama = nama_baru
                print('\n<< CATATAN KEUANGAN BERHASIL DIPERBARUI >>')
                return
            current = current.next
        print(f'<< CATATAN KEUANGAN DENGAN NAMA "{current.nama}" TIDAK DITEMUKAN >>')

    def delete_catatan_keuangan(self):
        while True:
            print('''
+--------------------------------+
| [1] Hapus dari Depan           |
| [2] Hapus di Antara            |
| [3] Hapus dari Belakang        |
+--------------------------------+
''')
            pilih = input('Pilih tempat untuk menghapus catatan keuangan (1/2/3): ')
            if pilih == '1':
                if self.head is None:
                    print('<< CATATAN KEUANGAN KOSONG >>')
                    return
                if self.head.next is None:
                    self.head = None
                    return
                self.head = self.head.next
                self.head.prev = None
                print('<< CATATAN KEUANGAN BERHASIL DIHAPUS DARI DEPAN')
                return

            elif pilih == '2':
                if self.head is None:
                        print('<< CATATAN KEUANGAN KOSONG >>')
                        return
                read_catke()
                nama = input('Masukkan nama catatan keuangan yang ingin dihapus: ').title()
                current_node = self.head
                prev_node = None
                while current_node:
                    if current_node.nama == nama:
                        if prev_node:
                            prev_node.next = current_node.next
                        else:
                            self.head = current_node.next
                        if current_node.next:
                            current_node.next.prev = prev_node
                        print('<< CATATAN KEUANGAN BERHASIL DIHAPUS >>')
                        return
                    prev_node = current_node
                    current_node = current_node.next
                print(f'<< CATATAN KEUANGAN DENGAN NAMA "{nama}" TIDAK DITEMUKAN >>')

            elif pilih == '3':
                if self.head is None:
                    print('<< CATATAN KEUANGAN KOSONG >>')
                    return
                if self.head.next is None:
                    self.head = None
                    return
                n = self.head
                while n.next is not None:
                    n = n.next
                n.prev.next = None
                print('<< CATATAN KEUANGAN BERHASIL DIHAPUS DARI BELAKANG >>')
                return

    def quick_sort(self, head, ascending=True):
        if head is None or head.next is None:
            return head

        pivot = head.nama
        smaller_head = None
        smaller_tail = None
        larger_head = None
        larger_tail = None
        current = head.next
        while current is not None:
            next_node = current.next
            current.next = None
            current.prev = None
            if (ascending and current.nama < pivot) or (not ascending and current.nama > pivot):
                if smaller_head is None:
                    smaller_head = current
                    smaller_tail = current
                else:
                    current.prev = smaller_tail
                    smaller_tail.next = current
                    smaller_tail = current
            else:
                if larger_head is None:
                    larger_head = current
                    larger_tail = current
                else:
                    current.prev = larger_tail
                    larger_tail.next = current
                    larger_tail = current
            current = next_node

        smaller_head = self.quick_sort(smaller_head, ascending)
        larger_head = self.quick_sort(larger_head, ascending)

        if smaller_head is None:
            smaller_head = head
            head.prev = None
        else:
            smaller_tail.next = head
            head.prev = smaller_tail

        if larger_head is None:
            head.next = None
        else:
            head.next = larger_head
            larger_head.prev = head

        return smaller_head

    
    def sort_ascending(self):
        self.head = self.quick_sort(self.head, True)
        self.read_catatan_keuangan() 
    
    def sort_descending(self):
        self.sort_ascending()
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            current.prev = next_node 
            prev = current
            current = next_node
        self.head = prev

    def sort_by_date(self, ascending=True):
        if self.head is None:
            print("<< CATATAN KEUANGAN KOSONG >>")
            return

        sorted_list = []
        current = self.head
        while current:
            sorted_list.append(current)
            current = current.next

        sorted_list.sort(key=lambda x: datetime.strptime(x.tanggal, '%d/%m/%Y'), reverse=not ascending)

        self.head = sorted_list[0]
        current = self.head
        for node in sorted_list[1:]:
            current.next = node
            node.prev = current
            current = current.next
        current.next = None

    def sort_by_latest_date(self):
        self.sort_by_date(ascending=False)
        self.read_catatan_keuangan()

    def sort_by_oldest_date(self):
        self.sort_by_date(ascending=True)
        self.read_catatan_keuangan()

        
dompet = DompetDigital()

dompet.create_catatan_keuangan('Makan', '10/01/2024', '20000', 'Tunai')
dompet.create_catatan_keuangan('Belanja', '10/10/2023', '100000', 'Non Tunai')
dompet.create_catatan_keuangan('Liburan', '09/09/2024', '50000000', 'Non Tunai')

        
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
            print('\n<< INPUT TANGGAL TIDAK SESUAI >>\n')

    while True:
        try:
            jumlah = int(input('\nMasukkan jumlah: Rp '))
            break
        except ValueError:
            print('\n<< INPUT JUMLAH UANG TIDAK SESUAI >>')
        
    while True:
        try:
            jenis_pembayaran = input('\nMasukkan jenis pembayaran (tunai/non tunai): ').title()
            break
        except ValueError:
            print('\n<< INPUT JENIS PEMBAYARAN TIDAK SESUAI >>')

    while True:
        try:
            nama = input('\nMasukkan nama catatan keuangan: ').title()
            break
        except ValueError:
            print('\n<< INPUT NAMA HARUS ALFABET >> ')

    dompet.create_catatan_keuangan(nama, tanggal, jumlah, jenis_pembayaran)

def read_catke():
    dompet.read_catatan_keuangan()     

def update_catke():
    read_catke()
    while True:
        nama_lama = input('Masukkan nama catatan keuangan yang ingin diperbarui: ').title()
        print('''
+--------------------------------+
|    PERBARUI CATATAN KEUANGAN   |
+--------------------------------+''')
        while True:
            try:
                tanggal_baru = input('Masukkan tanggal yang terbaru: ')
                datetime.strptime(tanggal_baru, "%d/%m/%Y")
                break
            except ValueError:
                print('<< INPUT TANGGAL TIDAK SESUAI >>')

        while True:
            try:
                jumlah_baru = int(input('\nMasukkan jumlah: Rp '))
                break
            except ValueError:
                print('\n<< INPUT JUMLAH UANG TIDAK SESUAI >>')        
        
        while True:
            try:
                jenis_pembayaran_baru = input('\nMasukkan jenis pembayaran (tunai/non tunai): ').title()
                break
            except ValueError:
                print('\n<< INPUT JENIS PEMBAYARAN TIDAK SESUAI >>')

        while True:
            try:
                nama_baru = input('\nMasukkan nama catatan keuangan: ').title()
                break
            except ValueError:
                print('\n<< INPUT NAMA HARUS ALFABET >> ')    
        dompet.update_catatan_keuangan(nama_lama, tanggal_baru, jumlah_baru, jenis_pembayaran_baru, nama_baru)
        break

def delete_catke():
    print('''
+--------------------------------+
|     HAPUS CATATAN KEUANGAN     |
+--------------------------------+''')
    read_catke()
    dompet.delete_catatan_keuangan()

def sorting():
    print('''
+--------------------------------+
|            Sorting             |
+--------------------------------+
| [1] Nama A-Z                   |
| [2] Nama Z-A                   |
| [3] Tanggal Terbaru            |
| [4] Tanggal Terlama            |
+---------------------------------+''')
    pilih = input('Sorting catatan keuangan berdasarkan (1/2/3/4): ')
    if pilih == '1':
        dompet.sort_ascending()
        dompet.read_catatan_keuangan()
    elif pilih == '2':
        dompet.sort_descending()
        dompet.read_catatan_keuangan()
    elif pilih == '3':
        dompet.sort_by_latest_date()
    elif pilih == '4':
        dompet.sort_by_oldest_date()

while True:
    print('''
+--------------------------------+
|        Catatan Keuangan        |
+--------------------------------+
| [1] Buat Catatan Keuangan      |
| [2] Lihat Catatan Keuangan     |
| [3] Perbarui Catatan Keuangan  |
| [4] Hapus Catatan Keuangan     |
| [5] Sorting Catatan Keuangan   |
| [0] Keluar dari Program        |
+--------------------------------+''')
    pilihan = input('Masukkan pilihan (1/2/3/4): ')
    if pilihan == '1':
        os.system ('cls')
        create_catke()
    elif pilihan == '2':
        read_catke()
    elif pilihan == '3':
        os.system ('cls')
        update_catke()
    elif pilihan == '4':
        os.system ('cls')
        delete_catke()
    elif pilihan == '5':
        os.system ('cls')
        sorting()
    elif pilihan == '0':
        print('\n<< PROGRAM DOMPET DIGITAL SELESAI >>')
        break
    else:
        print('<< Input tidak valid >>')
        
