# Konvensi: konstanta ditulis dengan HURUF KAPITAL, kata dipisah underscore
PI = 3.14159
MAX_USER = 100
APP_NAME = "Aplikasi Belajar Python"

print(PI)
print(MAX_USER)
print(APP_NAME)

# Python tidak benar-benar melarang konstanta diubah,
# hanya developer yang sepakat untuk tidak mengubahnya
PI = 3.14
print("PI setelah diubah:", PI)

# Mengimpor konstanta dari module constants.py
from constants import PI as PI_MODULE, GRAVITY, MAX_RETRY

print("Nilai PI:", PI_MODULE)
print("Gravitasi:", GRAVITY)
print("Maksimal percobaan:", MAX_RETRY)

# Contoh penggunaan: menghitung pajak
TAX_RATE = 0.1
harga_barang = 50000
total = harga_barang + (harga_barang * TAX_RATE)
print("Total harga:", total)