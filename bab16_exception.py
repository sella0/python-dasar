# ===== Apa itu exception? =====
# Tanpa penanganan, program langsung berhenti saat terjadi error.
# angka = 10
# hasil = angka / 0     # hapus tanda # untuk melihat ZeroDivisionError


# ===== Menangani exception dengan try-except =====
try:
    angka = 10
    hasil = angka / 0
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")


# ===== Menangani banyak jenis error =====
try:
    data = int("abc")        # string "abc" tidak bisa diubah jadi angka
except ValueError:
    print("Error: Data tidak valid!")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")


# ===== Menggunakan else dan finally =====
# else    -> dijalankan jika tidak ada error
# finally -> selalu dijalankan, baik ada error atau tidak
try:
    angka = 10 / 2
except ZeroDivisionError:
    print("Error: Tidak bisa bagi nol!")
else:
    print("Pembagian berhasil, hasil:", angka)
finally:
    print("Selesai memproses.")


# ===== Membuat exception sendiri dengan raise =====
def cek_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak boleh negatif!")
    print(f"Umur valid: {umur}")


try:
    cek_umur(-5)
except ValueError as e:
    print("Error:", e)