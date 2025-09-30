tugas = int(input("Masukkan nilai tugas: "))
uts = int(input("Masukkan nilai uts: "))
uas = int(input("Masukkan nilai uas: "))

jumlah = tugas + uts + uas
rata_rata = jumlah / 3

print(f"Rata-rata nilai: {rata_rata}")

if rata_rata >= 85:
    print("A")
elif 70 <= rata_rata < 85:
    print("B")
elif 60 <= rata_rata < 70:
    print("C")
else:
    print("D")