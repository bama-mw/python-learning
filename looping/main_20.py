n = int(input("Masukkan jumlah perkalian: "))
print("*", end="\t")
for i in range(1, n+1):
    print(i, end="\t")
print()

for i in range(1, n+1):
    print(i, end="\t")
    for j in range(1, n+1):
        print(i * j, end="\t")
    print()