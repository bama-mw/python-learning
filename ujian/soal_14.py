huruf = input("Masukkan sebuah huruf (A-Z): ").upper()

if huruf in 'AIUEO':
    print(huruf, "adalah vokal")
elif huruf in 'BCDFGHJKLMNPQRSTVWXYZ':
    print(huruf, "adalah konsonan")
else:
    print(huruf, "bukan huruf alfabet")