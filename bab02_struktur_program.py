# Ini komentar satu baris, tidak dijalankan oleh Python

"""
Ini komentar multi-baris.
Biasanya dipakai untuk dokumentasi.
"""

# Statement: satu perintah per baris
print("Halo, Python!")

# Indentasi: Python memakai 4 spasi untuk menandai blok kode
umur = 18
if umur >= 17:
    print("Kamu sudah boleh membuat KTP")
else:
    print("Kamu belum cukup umur")

# Input dan output
nama = input("Masukkan nama kamu: ")
print("Halo,", nama)


# Struktur program dengan fungsi main
def main():
    print("Halo dari fungsi main!")


if __name__ == "__main__":
    main()