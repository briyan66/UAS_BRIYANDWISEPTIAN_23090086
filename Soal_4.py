class Buah:
    def _init_(self, nama, warna, rasa):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def information(self):
        print(f"Nama: {self.nama}")
        print(f"Warna: {self.warna}")
        print(f"Rasa: {self.rasa}")

class Jeruk(Buah):
    def _init_(self, nama, warna, rasa, vitamin):
        super()._init_(nama, warna, rasa)
        self.vitamin = vitamin

    def setVitamin(self, vitamin):
        self.vitamin = vitamin

    def information(self):
        super().information()
        print(f"Vitamin: {self.vitamin}")

jeruk = Jeruk("jeruk", "oren", "kecut", "Z")
jeruk.information()
