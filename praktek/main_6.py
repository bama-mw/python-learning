suhu = int(input("Suhu: "))

if suhu < 0:
    print("Zat padat")
elif 0 <= suhu < 100:
    print("Zat cair")
else:
    print("Zat uap")