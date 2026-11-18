# Percabangan: if, elif, else
nilai = 85

if nilai >= 90:
    print("A")
elif nilai >= 75:
    print("B")
else:
    print("C")

# Perulangan for: mengulang setiap elemen di dalam koleksi
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(item)

# for dengan range: mengulang sejumlah angka tertentu
for i in range(1, 4):
    print("Angka:", i)

# Perulangan while: mengulang selama kondisi masih True
counter = 0

while counter < 3:
    print("Hitung:", counter)
    counter += 1

# break: menghentikan perulangan sepenuhnya
# continue: melewati iterasi saat ini, lanjut ke iterasi berikutnya
for i in range(1, 6):
    if i == 3:
        continue   # angka 3 dilewati
    if i == 5:
        break      # berhenti saat i = 5
    print(i)