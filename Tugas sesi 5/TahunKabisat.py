Tahun = int(input("Masukkan Tahun Kabisat :"))
Perhitungan = "Tahun Kabisat"if Tahun % 4 == 0 and Tahun % 100 != 0 or Tahun % 400 == 0 else "Bukan Merupakan Tahun Kabisat"
print("Tahun %s adalah %s " % (Tahun,Perhitungan) )