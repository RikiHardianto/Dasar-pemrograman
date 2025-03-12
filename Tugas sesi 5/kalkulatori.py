input1 = int(input("Masukan Angka Pertama :"))
operator = input("Masukan Operator +,-,*,/ :")
input2 = int(input("Masukan Angka Kedua :"))

hitungan = 0
if operator == "+":
    hitungan = input1 + input2
elif operator == "-":
    hitungan = input1 + input2
elif operator == "*":
    hitungan = input1 * input2
elif operator == "/":
    hitungan = input1 / input2
else:
    print("Hasil Tidak Ditemukan")

print("Hasul Dari 2 input di atas Adalah :", hitungan)