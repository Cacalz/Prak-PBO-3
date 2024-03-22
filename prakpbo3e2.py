class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar


# Membuat objek dari class PersegiPanjang
persegi_panjang = PersegiPanjang(20, 12)

# Menampilkan informasi
print("Calista Azzahra 064002300008 Teknik Industri")
print("-----PROGRAM MENGHITUNG LUAS PERSEGI PANJANG-----")
print(f"Persegi panjang dengan panjang {persegi_panjang.panjang}cm dan lebar {persegi_panjang.lebar}cm memiliki luas sebesar {persegi_panjang.hitung_luas()}cm^2")
