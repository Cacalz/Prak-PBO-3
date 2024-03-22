class Identitas:
    def __init__(self, nama, nim, fakultas, hobi):
        self.nama = nama
        self.nim = nim
        self.fakultas = fakultas
        self.hobi = hobi

    def tampilkan_identitas(self):
        print("Calista Azzahra (064002300008)")
        print("--PROGRAM MENAMPILKAN IDENTITAS--")
        print(f"Nama saya adalah {self.nama} NIM saya ({self.nim}).")
        print(f"Saya dari fakultas {self.fakultas}.")
        print(f"Hobi saya adalah {self.hobi}.")


# Membuat objek dari class Identitas
identitas_Calista = Identitas("Calista Azzahra", "064002300008", "Teknik Informatika", "Nonton Haruto")

# Memanggil metode untuk menampilkan identitas
identitas_Calista.tampilkan_identitas()
