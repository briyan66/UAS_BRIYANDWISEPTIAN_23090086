# queue_system.py

class Antrian:
    def __init__(self):
        self.antrian = []

    def tambah_pesanan(self, pesanan):
        self.antrian.append(pesanan)
        print(f"Pesanan {pesanan} ditambahkan ke antrian.")

    def hapus_pesanan(self):
        if not self.antrian:
            print("Tidak ada pesanan di antrian.")
        else:
            pesanan = self.antrian.pop(0)
            print(f"Pesanan {pesanan} disajikan.")

    def tampilkan_antrian(self):
        print("Antrian saat ini:")
        for i, pesanan in enumerate(self.antrian, start=1):
            print(f"{i}. {pesanan}")

def main():
    antrian = Antrian()

    while True:
        print("\nSistem Antrian Restoran")
        print("1. Tambah pesanan ke antrian")
        print("2. Sajikan pesanan")
        print("3. Tampilkan antrian")
        print("4. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            pesanan = input("Masukkan pesanan: ")
            antrian.tambah_pesanan(pesanan)
        elif pilihan == "2":
            antrian.hapus_pesanan()
        elif pilihan == "3":
            antrian.tampilkan_antrian()
        elif pilihan == "4":
            print("Keluar program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")