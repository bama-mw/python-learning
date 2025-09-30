def kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    return False

tl = int(input("Masukkan tahun lahir: "))
ts = int(input("Masukkan tahun sekarang: "))

jumlah_kabisat = 0
for tahun in range(tl, ts + 1):
    if kabisat(tahun):
        jumlah_kabisat += 1

print(f"Jumlah tahun kabisat dari {tl} hingga {ts} adalah {jumlah_kabisat}")