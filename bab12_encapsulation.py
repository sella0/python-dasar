# ===== Public, Protected, dan Private =====
class Contoh:
    def __init__(self):
        self.nama = "publik"      # public: bebas diakses dari mana saja
        self._klien = "protected" # protected: awalan _, konvensi "jangan diakses dari luar"
        self.__rahasia = "privat" # private: awalan __, tidak bisa diakses langsung dari luar

    def tampilkan_rahasia(self):
        return self.__rahasia


c = Contoh()
print(c.nama)                  # publik
print(c._klien)                # protected (bisa, tapi tidak disarankan)
print(c.tampilkan_rahasia())   # privat, lewat method di dalam class
# print(c.__rahasia)           # hapus tanda # untuk melihat AttributeError


# ===== Contoh encapsulation dengan private attribute =====
class RekeningBank:
    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self.__saldo = saldo_awal      # private attribute

    # getter: method untuk membaca saldo
    def lihat_saldo(self):
        return self.__saldo

    # method untuk mengubah saldo dengan validasi
    def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah setor harus positif!")

    def tarik(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak cukup atau jumlah tidak valid!")


# Membuat object
akun = RekeningBank("Budi", 1000)

# Mengakses saldo lewat method (bukan langsung)
print("Saldo awal:", akun.lihat_saldo())

akun.setor(500)
print("Setelah setor:", akun.lihat_saldo())

akun.tarik(300)
print("Setelah tarik:", akun.lihat_saldo())

# Percobaan yang ditolak oleh validasi
akun.setor(-100)
akun.tarik(99999)

# Mengakses atribut private langsung akan error
# print(akun.__saldo)    # hapus tanda # untuk melihat AttributeError