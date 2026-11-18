# ===== Membuat class dan object =====
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def sapa(self):
        print(f"Halo, nama saya {self.nama} dari jurusan {self.jurusan}")


# Membuat object dari class
mhs1 = Mahasiswa("Budi", "Informatika")
mhs2 = Mahasiswa("Sella", "Sistem Informasi")

# Memanggil method
mhs1.sapa()
mhs2.sapa()


# ===== Atribut dan method =====
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang   # atribut
        self.lebar = lebar       # atribut

    def luas(self):              # method
        return self.panjang * self.lebar

    def keliling(self):          # method
        return 2 * (self.panjang + self.lebar)


pp = PersegiPanjang(5, 3)
print("Luas:", pp.luas())            # 15
print("Keliling:", pp.keliling())    # 16


# ===== Encapsulation: menyembunyikan data =====
class RekeningBank:
    def __init__(self, saldo):
        self._saldo = saldo      # tanda _ berarti atribut "privat" (konvensi)

    def lihat_saldo(self):
        return self._saldo

    def setor(self, jumlah):
        self._saldo += jumlah


akun = RekeningBank(1000)
akun.setor(500)
print("Saldo:", akun.lihat_saldo())  # 1500