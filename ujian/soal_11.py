total_harga = float(input("Masukkan total harga barang: "))

if total_harga >= 100000:
    diskon = total_harga * 0.05
else:
    diskon = 0
total_bayar = total_harga - diskon

print("Diskon:", diskon)
print("Total yang harus dibayar:", total_bayar)