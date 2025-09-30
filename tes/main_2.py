inputan = int(input("Input 1-100: "))

if inputan >= 1 and inputan <= 50:
    print("Kelompok A")
    if inputan >= 1 and inputan <= 25:
        print("A1")
    elif inputan >= 26 and inputan <= 50:
        print("A2")

elif inputan >= 51 and inputan <= 100:
    print("Kelompok B")
    if inputan >= 51 and inputan <= 75:
        print("B1")
    elif inputan >= 76 and inputan <= 100:
        print("B2")

# Waktu pengerjaan 4 menit.