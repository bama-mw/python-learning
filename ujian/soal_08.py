tinggi = float(input("Masukkan tinggi tabung: "))
jari_jari = float(input("Masukkan jari jari tabung: "))

volume_tabung = 2 * 3.14 * jari_jari * tinggi
luas_permukaan_tabung = 3.14 * jari_jari * jari_jari + 2 * 3.14 * jari_jari * tinggi

print("Volume Tabung:", volume_tabung, "cm3")
print("Luas Permukaan Tabung:", luas_permukaan_tabung, "cm2")