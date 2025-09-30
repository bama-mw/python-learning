pertanyaan = "Siapa ketua kelas x pplg 2?"
pilihan_jawaban = [
    "a. Aden",
    "b. Putri",
    "c. Nesya",
    "d. Dimit",
    "e. Resna"
]

jawaban_benar = "c"

print(pertanyaan)
for pilihan in pilihan_jawaban:
    print(pilihan)

jawaban_pengguna = input("Masukkan jawaban yang benar (a-e): ").lower()

if jawaban_pengguna == jawaban_benar:
    print("Jawaban benar!")
else:
    print(f"Jawaban salah. Jawaban yang benar adalah {jawaban_benar}.")