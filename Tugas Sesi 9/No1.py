angka = []

for i in range (10) :
    number = float(input(f"Masukkan angka ke {i+1} :"))
    angka.append(number)
    
    jumlah = sum(angka)
    
    print("List angka :", angka )
    print("Jumlah Dari element dalam List yaitu :",jumlah)
    

 