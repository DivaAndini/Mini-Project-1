import os
os.system ('cls')

class Akun:
    def __init__(self, nama, email, pin, no_hp, saldo):
        self.nama = nama
        self.email = email
        self.pin = pin
        self.no_hp = no_hp
        self.saldo = saldo

class DompetDigital:
    def __init__(self):
        self.akun_list = []

    def tambah_akun(self, akun):
        self.akun_list.append(akun)
        print(f'<< Akun {akun.nama} telah berhasil dibuat >>')

    def lihat_akun(self, akun):
        while True:
            if akun in self.akun_list:
                print(f'''
+------------------------------------+
            Informasi Akun          
+------------------------------------+
Nama: {akun.nama}
Email: {akun.email}
PIN: {akun.pin}
No HP: {akun.no_hp}
+------------------------------------+''')
            else:
                print('     << Akun tidak terdaftar >>')
            break
            
    def update_akun(self, akun, email_baru, pin_baru, no_hp_baru):
        if akun in self.akun_list:
            akun.email = email_baru
            akun.pin = pin_baru
            akun.no_hp = no_hp_baru
            print(f"\n<< Informasi akun {akun.nama} telah diperbarui >>")
        else:
            raise ValueError("     << Akun tidak ditemukan >>")

    def hapus_akun(self, akun, nama):
        while True:
            if nama in self.akun_list:
                self.akun_list.remove(akun)
                print(f"<< Akun {akun.nama} telah dihapus >>")
            else:
                raise ValueError("     << Akun tidak ditemukan >>")

    def cek_saldo(self, akun):
        if akun in self.akun_list:
            print('\n+------------------------------------+')
            print(f"Saldo Anda saat ini: Rp{akun.saldo}")
            print('+------------------------------------+')
        else:
            raise ValueError("     << Akun tidak ditemukan >>")

    def tambah_saldo(self, akun, nominal):
        if akun in self.akun_list:
                akun.saldo += nominal
                print(f"\n<< Transaksi senilai Rp{nominal} berhasil >>")
        else: 
            raise ValueError("     << Akun tidak ditemukan >>")
        
    def kirim_saldo(self, akun, nominal):
        if akun in self.akun_list:
            if akun.saldo >= nominal:
                akun.saldo -= nominal
                print(f"\n<< Transaksi senilai Rp{nominal} berhasil >>")
            else:
                print('<< Saldo tidak cukup untuk melakukan transaksi >>')
        else:
            raise ValueError("     << Akun tidak ditemukan >>")

def login():
    print('\n+--------------------------------+')
    print('               Login            ')
    print('+--------------------------------+')
    email = input('Masukkan email: ')
    pin = int(input('Masukkan PIN: '))

    for akun_terdaftar in dompet.akun_list:
        if akun_terdaftar.email == email and akun_terdaftar.pin == pin:
            print(f"Selamat datang, {akun_terdaftar.nama}!")
            while True:
                print('''
+--------------------------------+
|            Menu Akun           |
+--------------------------------+
| [1] Lihat Saldo                |
| [2] Tambah Saldo               |
| [3] Kirim Saldo                |
| [4] Informasi Akun             |
| [5] Keluar                     |
+--------------------------------+''')
                pilihan = input("Masukkan pilihan: ")
                if pilihan == '1':
                    dompet.cek_saldo(akun_terdaftar)
                elif pilihan == '2':
                    nominal = int(input("Masukkan nominal: Rp"))
                    dompet.tambah_saldo(akun_terdaftar, nominal)
                elif pilihan == '3':
                    nominal = int(input('Masukkan nominal: Rp'))
                    dompet.kirim_saldo(akun_terdaftar, nominal)
                elif pilihan == '4':
                    dompet.lihat_akun(akun_terdaftar)
                    tanya = input('Apakah ingin memperbarui informasi akun? (y/t): ')
                    if tanya == 'y':
                        email_baru = input('\nMasukkan email yang terbaru: ')
                        pin_baru = int(input('Masukkan PIN yang terbaru: '))
                        no_hp_baru = int(input('Masukkan No HP terbaru: '))
                        dompet.update_akun(akun_terdaftar, email_baru, pin_baru, no_hp_baru)
                    else:
                        print('\n     << Kembali ke menu akun >>')
                elif pilihan == '5':
                    print('     << Keluar dari akun')
                    break
                else:
                    print('     << Pilihan tidak valid >>')
    else:
        print("\n     << Akun tidak ditemukan >>")

def buat_akun_baru():
    print('\n+--------------------------------+')
    print('           Daftar Akun            ')
    print('+--------------------------------+')
    nama = input('Masukkan nama lengkap: ')
    no_hp = int(input('Masukkan nomor ponsel: '))
    email = input('Masukkan email baru: ')
    pin = int(input('Masukkan PIN baru: '))
    print('+--------------------------------+\n')
    akun_baru = Akun(nama, email, pin, no_hp, saldo=0)
    dompet.tambah_akun(akun_baru)
    
dompet = DompetDigital()

while True:
    print('''
+--------------------------------+
|        Dompet Digital          |
+--------------------------------+
| [1] Login                      |
| [2] Buat Akun                  |
+--------------------------------+''')
    pilih = input("Masukkan pilihan: ")
    if pilih == '1':
        login()
    elif pilih == '2':
        buat_akun_baru()
    else:
        print('     << Pilihan tidak valid >>')



