from abc import ABC, abstractmethod


# ===== Abstract class =====
class Hewan(ABC):
    @abstractmethod
    def suara(self):
        pass                      # hanya kerangka, tanpa isi


# Subclass wajib mengimplementasikan semua abstract method
class Kucing(Hewan):
    def suara(self):
        return "Meow"


class Anjing(Hewan):
    def suara(self):
        return "Guk guk"


# Abstract class tidak bisa langsung dibuat objeknya
# h = Hewan()                     # hapus tanda # untuk melihat TypeError

k = Kucing()
a = Anjing()

print(k.suara())
print(a.suara())


# ===== Abstraction di dunia nyata: sistem pembayaran =====
class Pembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah):
        pass


class Gopay(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan GoPay")


class Dana(Pembayaran):
    def bayar(self, jumlah):
        print(f"Bayar {jumlah} menggunakan Dana")


# Function ini bekerja untuk metode pembayaran apa pun
def proses_pembayaran(metode, jumlah):
    metode.bayar(jumlah)


proses_pembayaran(Gopay(), 50000)
proses_pembayaran(Dana(), 75000)