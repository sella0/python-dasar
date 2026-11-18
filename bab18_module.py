# ===== Menggunakan module buatan sendiri =====
import matematika

print(matematika.tambah(5, 3))    # 8
print(matematika.kali(4, 3))      # 12


# ===== Import dengan alias =====
import matematika as m

print(m.tambah(10, 5))            # 15


# ===== Import fungsi tertentu =====
from matematika import tambah

print(tambah(7, 3))               # 10, tanpa awalan nama module


# ===== Built-in modules (module bawaan Python) =====
import math

print(math.sqrt(16))              # 4.0, akar kuadrat
print(math.pi)                    # 3.141592653589793