# ===== Polymorphism pada method =====
class Kucing:
    def suara(self):
        return "Meow"


class Anjing:
    def suara(self):
        return "Guk guk"


hewan = [Kucing(), Anjing()]

for h in hewan:
    print(h.suara())     # nama method sama, hasilnya berbeda


# ===== Polymorphism dengan inheritance =====
class Hewan:
    def suara(self):
        return "Hewan bersuara"


class Kucing2(Hewan):
    def suara(self):                 # overriding method parent
        return "Meow"


class Anjing2(Hewan):
    def suara(self):
        return "Guk guk"


daftar_hewan = [Kucing2(), Anjing2(), Hewan()]

for h in daftar_hewan:
    print(h.suara())


# ===== Polymorphism dengan function =====
def cetak_suara(hewan):
    print(hewan.suara())


cetak_suara(Kucing())
cetak_suara(Anjing())


# ===== Polymorphism dengan built-in function =====
print(len("Python"))        # 6, menghitung jumlah karakter
print(len([1, 2, 3]))      # 3, menghitung jumlah elemen list
print(len(("a", "b")))     # 2, menghitung jumlah elemen tuple