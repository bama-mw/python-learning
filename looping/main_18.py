n = int(input("Masukkan jumlah perkalian: "))
for i in range(1, 6):
    for j in range(1, n+1):
        print(f"{j} x {i} = {j*i}", end="\t")
    print()