# ===== LIST: kumpulan data berurutan, bisa diubah (mutable) =====
buah = ["apel", "jeruk", "mangga"]

# Mengakses elemen lewat indeks (dimulai dari 0)
print(buah[0])             # apel

# Menambah elemen di akhir list
buah.append("semangka")

# Mengubah elemen
buah[2] = "anggur"

# Menghapus elemen berdasarkan nilainya
buah.remove("jeruk")

print(buah)                # ['apel', 'anggur', 'semangka']


# ===== TUPLE: mirip list, tapi tidak bisa diubah (immutable) =====
warna = ("merah", "hijau", "biru")

print(warna[1])            # hijau

# Perulangan pada tuple
for w in warna:
    print(w)

# warna[0] = "kuning"      # hapus tanda # untuk melihat TypeError


# ===== SET: kumpulan data unik, tidak berurutan =====
angka = {1, 2, 3, 3, 4, 5}
print(angka)               # {1, 2, 3, 4, 5}, angka 3 yang dobel dibuang

# Menambah dan menghapus elemen
angka.add(6)
angka.remove(2)
print(angka)               # {1, 3, 4, 5, 6}

# Operasi himpunan
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(set1 | set2)         # gabungan (union): {1, 2, 3, 4, 5, 6, 7, 8}
print(set1 & set2)         # irisan (intersection): {4, 5}
print(set1 - set2)         # selisih (difference): {1, 2, 3}