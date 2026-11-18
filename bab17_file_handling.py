# ===== Menyiapkan file contoh (supaya bisa dibaca di bawah) =====
file = open("data.txt", "w")
file.write("Halo Dunia")
file.close()


# ===== Membuka dan membaca file =====
# Mode "r" = read (baca)
file = open("data.txt", "r")
print(file.read())          # membaca seluruh isi file
file.close()                # file harus selalu ditutup setelah selesai


# ===== Membaca file baris per baris =====
file = open("data.txt", "w")
file.write("Baris 1\nBaris 2\nBaris 3\n")
file.close()

file = open("data.txt", "r")
for baris in file:
    print(baris.strip())    # strip() menghapus karakter newline di akhir baris
file.close()


# ===== Menulis ke file =====
# Mode "w" = write. Kalau file sudah ada, isinya DITIMPA (overwrite)
file = open("data.txt", "w")
file.write("Halo, ini data baru!\n")
file.write("Baris kedua...\n")
file.close()


# ===== Menambah data ke file =====
# Mode "a" = append. Data baru ditambahkan di akhir tanpa menghapus isi lama
file = open("data.txt", "a")
file.write("Baris tambahan...\n")
file.close()

# Cek hasil akhir isi file
file = open("data.txt", "r")
print(file.read())
file.close()


# ===== Menggunakan with (best practice) =====
# File otomatis ditutup setelah blok with selesai, tanpa perlu close()
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)


# ===== Contoh program lengkap =====
# 1. Menulis file
with open("contoh.txt", "w") as file:
    file.write("Belajar Python itu menyenangkan!\n")

# 2. Menambah data ke file
with open("contoh.txt", "a") as file:
    file.write("Tambahan baris baru.\n")

# 3. Membaca file baris per baris
with open("contoh.txt", "r") as file:
    for baris in file:
        print(baris.strip())