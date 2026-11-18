# ===== Inheritance dasar =====
# Parent class (superclass)
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print(f"{self.nama} membuat suara")


# Child class (subclass): mewarisi atribut dan method dari Hewan
class Kucing(Hewan):
    def suara(self):                      # overriding: menimpa method parent
        print(f"{self.nama} mengeong: Meow!")


class Anjing(Hewan):
    def suara(self):
        print(f"{self.nama} menggonggong: Guk guk!")


kucing = Kucing("Tom")
anjing = Anjing("Spike")

kucing.suara()
anjing.suara()


# ===== Menambahkan method baru di subclass =====
class Burung(Hewan):
    def suara(self):
        print(f"{self.nama} berkicau: Cuit cuit!")

    def terbang(self):                    # method baru, hanya ada di Burung
        print(f"{self.nama} sedang terbang")


burung = Burung("Pio")
burung.suara()
burung.terbang()


# ===== Menggunakan super() untuk mengakses parent =====
class Mahasiswa:
    def __init__(self, nama, jurusan):
        self.nama = nama
        self.jurusan = jurusan

    def info(self):
        print(f"Nama: {self.nama}, Jurusan: {self.jurusan}")


class MahasiswaBaru(Mahasiswa):
    def __init__(self, nama, jurusan, tahun_masuk):
        super().__init__(nama, jurusan)   # memanggil constructor parent
        self.tahun_masuk = tahun_masuk

    def info(self):
        super().info()                    # memanggil method info() milik parent
        print(f"Tahun Masuk: {self.tahun_masuk}")


mhs = MahasiswaBaru("Andi", "Informatika", 2023)
mhs.info()