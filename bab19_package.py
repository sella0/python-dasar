# ===== Menggunakan package =====
from my_package import operasi, geometri

print(operasi.kurang(10, 2))        # 8
print(geometri.luas_persegi(5))     # 25


# ===== Import fungsi tertentu dari package =====
from my_package.operasi import kurang
from my_package.geometri import luas_persegi

print(kurang(20, 7))                # 13
print(luas_persegi(6))              # 36


# ===== Package di Python Standard Library =====
import os
import datetime
import json

print(os.getcwd())                  # folder kerja saat ini
print(datetime.datetime.today())    # tanggal dan waktu sekarang

data = {"nama": "Budi", "umur": 20}
teks_json = json.dumps(data)        # dictionary -> teks JSON
print(teks_json)
print(json.loads(teks_json))        # teks JSON -> dictionary