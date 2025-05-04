input_str = input("Masukkan Angka dan Dipisahkan Oleh Spasi: ")

angka_list = list(map(float, input_str.split()))

total = sum(angka_list)
 
rata_rata = total / len(angka_list)

terbesar = max (angka_list)
terkecil = min (angka_list)

print(f"List angka : ",angka_list)
print(f"Jumlah Total angka dari lsit :",total)
print(f"Nilai rata-rata angkanya :",rata_rata)
print(f"Nilai Terbesar Dari List :",terbesar)
print(f"Nilai Terkecil Dari List :",terkecil)