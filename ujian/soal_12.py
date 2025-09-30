nilai_siswa = int(input("Masukkan nilai siswa (0-100): "))

if 90 <= nilai_siswa <= 100:
    nilai = 'A'
elif 80 <= nilai_siswa < 90:
    nilai = 'B'
elif 70 <= nilai_siswa < 80:
    nilai = 'C'
elif 60 <= nilai_siswa < 70:
    nilai = 'D'
else:
    nilai = 'E'

print("nilai:", nilai)