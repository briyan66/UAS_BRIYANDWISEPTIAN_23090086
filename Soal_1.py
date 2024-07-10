mahasiswa = []

while True:
    nim = input("Masukan NIM: ")
    nama = input("Masukan Nama: ")
    mahasiswa.append({"NIM": nim, "Nama": nama})
    tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ")

    if tambah_lagi.lower() != "ya":
        break

print("Data Mahasiswa:")
for student in mahasiswa:
    print(f"NIM: {student['NIM']}, Nama: {student['Nama']}")
