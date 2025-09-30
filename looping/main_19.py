jumlah = int(input("Berapa banyak nilai yang ingin dimasukkan: "))
total = 0

for i in range(jumlah):
    nilai = int(input(f"Masukkan nilai ke-{i+1}: "))
    total += nilai

rata_rata = total / jumlah
print(f"Jumlah total: {total}")
print(f"Rata-rata: {rata_rata}")