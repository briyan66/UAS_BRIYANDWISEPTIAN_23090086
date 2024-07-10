import pandas as pd

data = {
    'Algoritma dan Struktur Data 2': [65, 50, 90],
    'Matematika Numerik': [70, 60, 80]
}
df = pd.DataFrame(data, index=['Mahasiswa 1', 'Mahasiswa 2', 'Mahasiswa 3'])
avg_subject = df.mean()
avg_student = df.mean(axis=1)

print("DataFrame:")
print(df)
print("\nRata-rata nilai untuk setiap mata kuliah:")
print(avg_subject)
print("\nRata-rata nilai untuk setiap mahasiswa:")
print(avg_student)