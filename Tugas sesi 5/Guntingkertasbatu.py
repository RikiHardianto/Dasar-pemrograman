import random

def main():
    pilihan = ("gunting", "kertas", "batu")
    skor_user = 0
    skor_komputer = 0

    while True:
        print("\nGunting, Kertas, Batu!")
        inuser = input("Masukkan pilihanmu (gunting/kertas/batu): ").lower()

        if inuser not in pilihan:
            print("Pilihan tidak valid, coba lagi!")
            continue

        pick_komputer = random.choice(pilihan)
        print(f"Komputer memilih: {pick_komputer}")

        if (inuser == "gunting" and pick_komputer == "kertas") or \
           (inuser == "kertas" and pick_komputer == "batu") or \
           (inuser == "batu" and pick_komputer == "gunting"):
            kategori = "Kamu menang!"
            skor_user += 1
        elif inuser == pick_komputer:
            kategori = "Seri!"
        else:
            kategori = "Komputer menang!"
            skor_komputer += 1

        print(f"{kategori} (Kamu: {skor_user} | Komputer: {skor_komputer})")

        pilih2 = input("Apakah kamu ingin bermain lagi? (Y/T): ").lower()
        if pilih2 != 'y':
            print("Terima kasih sudah bermain!")
            break


main()
