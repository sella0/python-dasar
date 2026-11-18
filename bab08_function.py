# Function sederhana
def sapa():
    print("Halo, selamat datang di Python!")

sapa()


# Function dengan parameter
def sapa_nama(nama):
    print("Halo", nama, "semoga harimu menyenangkan!")

sapa_nama("Budi")
sapa_nama("Sella")


# Function dengan return value
def tambah(a, b):
    return a + b

hasil = tambah(10, 7)
print("Hasil penjumlahan:", hasil)


# Default parameter: dipakai kalau argumen tidak diisi
def sapa_default(nama="Teman"):
    print("Halo", nama)

sapa_default("Budi")   # memakai argumen yang diberikan
sapa_default()         # memakai nilai default


# *args: menerima banyak argumen sebagai tuple
def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3, 4, 5)


# **kwargs: menerima banyak argumen berpasangan key=value sebagai dictionary
def biodata(**data):
    for key, value in data.items():
        print(key + ":", value)

biodata(nama="Budi", umur=20, kota="Jakarta")