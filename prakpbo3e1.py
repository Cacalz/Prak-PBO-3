class Identitas:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi

    def tampilkan_identitas(self):
        print("Calista Azzahra (064002300008)\n--PROGRAM MENAMPILKAN IDENTITAS--\nNama saya adalah {0} NIM saya ({1}).\nSaya dari fakultas {2}.\nHobi saya adalah {3}.".format(self.nama, self.nim, self.fakultas, self.hobi))


# Membuat objek dari class Identitas
identitas_Calista = Identitas("Calista Azzahra", "064002300008", "Teknik Informatika", "Nonton Haruto")

# Memanggil metode untuk menampilkan identitas
identitas_Calista.tampilkan_identitas()
