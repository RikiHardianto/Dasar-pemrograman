sisipertama = int(input("Masukan Panjang Sisi Pertama :"))
sisikedua = int(input("Masukan Panjang Sisi Kedua :"))
sisiketiga = int(input("Masukan Panjang Sisi Ketiga :"))

print(sisipertama,sisikedua,sisiketiga)

if sisipertama == sisikedua == sisiketiga :
    print("Segitiga sama sisi")

elif sisipertama==sisikedua or sisipertama==sisiketiga or sisikedua==sisiketiga :
    print("Sisi Sama Kaki")

else :
    print("Segitiga Asal-asalan")
