import statistics

input_str = input("Masukkan 5 angka yang di pisahkan oleh spasi : ")
angka_list = list(map(float,input_str.split()))

total = sum(angka_list)
nilai_minimum = min(angka_list)
nilai_maksimum = max(angka_list)
rata_rata = total / len(angka_list)
median = statistics.median(angka_list)
angka_terurut = sorted(angka_list)

print(f"Jumlah Angka =",total)
print(f"Nilai maxsimum =",nilai_maksimum)
print(f"Nilai Minimum =",nilai_minimum)
print(f"Nilai Rata-Rata =",rata_rata)
print(f"Nilia Median:",median)
print(f"List Urutan =",angka_terurut)

 