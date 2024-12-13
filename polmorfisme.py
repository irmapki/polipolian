class Makanan:
    def __init__(self, nama="", rasa=""):
        self.nama = nama
        self.rasa = rasa

    def deskripsi(self):
        print("Ini adalah sebuah makanan.")

    # Metode yang akan menunjukkan polymorphism
    def tampilkan_nama(self):
        print(f"Nama makanan ini adalah: {self.nama}")

    def tampilkan_rasa(self):
        print(f"Rasa makanan ini adalah: {self.rasa}")

    def sajikan(self):
        print("Makanan ini disajikan dengan cara standar.")

class MakananCepatSaji(Makanan):
    def sajikan(self):
        print("Makanan ini disajikan dengan cepat dalam kemasan praktis.")

class MakananTradisional(Makanan):
    def sajikan(self):
        print("Makanan ini disajikan dengan hiasan khas dan tradisional.")

# Fungsi polymorphism
def info_makanan(makanan):
    makanan.deskripsi()
    makanan.tampilkan_nama()
    makanan.tampilkan_rasa()
    makanan.sajikan()
    print()  # Baris kosong untuk memisahkan output

# Membuat objek dengan tipe yang berbeda
burger = MakananCepatSaji(nama="Burger", rasa="Gurih dan asin")
rendang = MakananTradisional(nama="Rendang", rasa="Pedas dan kaya rempah")

# Menggunakan fungsi yang sama untuk objek dengan tipe berbeda
info_makanan(burger) 
info_makanan(rendang) 
