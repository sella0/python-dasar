# Membuat dictionary: data berpasangan key-value
mahasiswa = {
    "nama": "Budi",
    "umur": 20,
    "jurusan": "Informatika"
}

print(mahasiswa)

# Mengakses data
print(mahasiswa["nama"])        # Budi
print(mahasiswa.get("umur"))    # 20

# get() tidak error kalau key tidak ada, hasilnya None
print(mahasiswa.get("alamat"))  # None
# print(mahasiswa["alamat"])    # hapus tanda # untuk melihat KeyError

# Menambah dan mengubah data
mahasiswa["angkatan"] = 2023    # menambah key baru
mahasiswa["umur"] = 21          # mengubah nilai key yang sudah ada
print(mahasiswa)

# Menghapus data
mahasiswa.pop("jurusan")        # menghapus dengan method pop
del mahasiswa["nama"]           # menghapus dengan del
print(mahasiswa)                # {'umur': 21, 'angkatan': 2023}

# Iterasi dictionary: perulangan pada key dan value
for key, value in mahasiswa.items():
    print(key, ":", value)

# Nested dictionary: dictionary di dalam dictionary
kelas = {
    "mahasiswa1": {"nama": "Budi", "umur": 21},
    "mahasiswa2": {"nama": "Sella", "umur": 20}
}

print(kelas["mahasiswa1"]["nama"])   # Budi
print(kelas["mahasiswa2"]["umur"])   # 20