# Membuat variabel
nama = "Sella"
umur = 20
tinggi = 170.5
is_active = True

print(nama)
print(umur)
print(tinggi)
print(is_active)

# Aturan penamaan: boleh huruf, angka, dan underscore (_)
# Gunakan snake_case untuk nama yang terdiri dari beberapa kata
first_name = "Budi"
total_harga = 15000
print(first_name, total_harga)

# Variabel bersifat case sensitive
nama_saya = "Sella"
Nama_Saya = "Budi"
print(nama_saya, Nama_Saya)  # dua variabel yang berbeda

# Multiple assignment: beberapa variabel sekaligus
a, b, c = 10, 20, 30
print(a, b, c)

# Satu nilai untuk beberapa variabel
x = y = z = 100
print(x, y, z)

# Mengecek tipe data variabel
print(type(nama))
print(type(umur))
print(type(tinggi))

# Menghapus variabel dengan del
n = 10
print(n)
del n
# print(n)  # hapus tanda # di depan baris ini untuk melihat NameError