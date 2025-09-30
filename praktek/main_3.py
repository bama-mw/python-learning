harga1 = int(input("Masukkan harga barang pertama: "))
harga2 = int(input("Masukkan harga barang kedua: "))
harga3 = int(input("Masukkan harga barang ketiga: "))

jumlah = harga1 + harga2 + harga3

print(f"Jumlah harga: {jumlah}")

poin = 1 if jumlah > 20000 else 0

print(f"Anda mendapatkan {poin} poin.")