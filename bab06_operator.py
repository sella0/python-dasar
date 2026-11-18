# Operator aritmatika
a = 10
b = 3

print("Penjumlahan:", a + b)           # 13
print("Pengurangan:", a - b)           # 7
print("Perkalian:", a * b)             # 30
print("Pembagian:", a / b)             # 3.3333...
print("Pembagian bulat:", a // b)      # 3
print("Sisa bagi (modulus):", a % b)   # 1
print("Pangkat:", a ** b)              # 1000

# Operator perbandingan (hasilnya True atau False)
x = 5
y = 10

print(x == y)   # False, sama dengan
print(x != y)   # True, tidak sama dengan
print(x > y)    # False
print(x < y)    # True
print(x >= y)   # False
print(x <= y)   # True

# Operator logika
p = True
q = False

print(p and q)  # False, True jika keduanya True
print(p or q)   # True, True jika salah satu True
print(not p)    # False, membalik nilai

# Gabungan perbandingan dan logika
umur = 20
print(umur >= 17 and umur <= 25)  # True

# Operator penugasan
n = 10
print(n)

n += 5   # sama dengan n = n + 5
print(n)  # 15

n -= 3   # sama dengan n = n - 3
print(n)  # 12

n *= 2   # sama dengan n = n * 2
print(n)  # 24

n /= 4   # sama dengan n = n / 4
print(n)  # 6.0

# Operator keanggotaan (membership): cek apakah nilai ada di dalam kumpulan data
buah = ["apel", "jeruk", "mangga"]

print("apel" in buah)       # True
print("pisang" not in buah) # True
print("pisang" in buah)     # False

# Operator identitas: cek apakah dua variabel menunjuk objek yang sama di memori
m = [1, 2, 3]
k = m           # k menunjuk objek yang sama dengan m
l = [1, 2, 3]   # objek baru dengan isi yang sama

print(m is k)       # True, objek yang sama
print(m is l)       # False, objek berbeda walau isinya sama
print(m is not l)   # True
print(m == l)       # True, isinya sama