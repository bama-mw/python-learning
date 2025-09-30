dico = 750000

if dico > 500000:
    total_harga = dico - (dico * 0.1)
else:
    total_harga = dico

print(f"Total harga: {total_harga}")