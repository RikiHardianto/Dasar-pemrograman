nilai_ujian = int(input("Masukkan NIlai Ujian :"))

if (nilai_ujian) >= 80 :
    print(f"{nilai_ujian} Adalah Nilai Dengan Grade A")
elif 70 <= nilai_ujian <= 79 :
    print(f"{nilai_ujian} Adalah Nilai ujian Dengan Grade B")
elif 60 <= nilai_ujian <= 69 :
    print(f"{nilai_ujian} Adalah Nilai Ujian Dengan Grade C")
elif 50 <= nilai_ujian <= 59 :
    print(f"{nilai_ujian} Adalah Nilai ujian Dengan Grade D")
elif 0 <= nilai_ujian <= 49 :
    print(f"{nilai_ujian} Adalah Nilai Ujian Dengan Grade E")
else :
    print("Maaf Anda Tidak Lulus ")

