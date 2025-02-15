import math

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitungLuas(self):
        return math.pi * self.jari_jari ** 2

# Contoh penggunaan:
persegi = Persegi(5)
lingkaran = Lingkaran(3)

print(f"Luas Persegi: {persegi.hitungLuas()}")  # Output: Luas Persegi: 25
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}")  # Output: Luas Lingkaran: 28.274333882308138
