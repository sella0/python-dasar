# Integer: bilangan bulat
umur = 20
print(umur, type(umur))

# Float: bilangan desimal
tinggi = 170.5
print(tinggi, type(tinggi))

# String: teks, boleh pakai tanda kutip tunggal atau ganda
nama = "Sella"
print(nama, type(nama))

# Boolean: True atau False
is_active = True
print(is_active, type(is_active))

# List: kumpulan data yang bisa diubah (mutable)
buah = ["apel", "jeruk", "mangga"]
buah.append("pisang")
print(buah, type(buah))

# Tuple: mirip list, tapi tidak bisa diubah (immutable)
warna = ("merah", "hijau", "biru")
print(warna, type(warna))

# Dictionary: data berpasangan key-value
mahasiswa = {"nama": "Budi", "umur": 21, "jurusan": "Informatika"}
print(mahasiswa["nama"], type(mahasiswa))

# Set: kumpulan data unik (tidak ada duplikat)
angka = {1, 2, 3, 3, 4}
print(angka, type(angka))

# Konversi tipe data
x = 10
y = float(x)
z = str(x)
print(y, type(y))
print(z, type(z))
print(int("25") + 5)