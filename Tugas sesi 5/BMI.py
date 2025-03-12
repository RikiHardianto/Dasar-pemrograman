print ("Menghitung BMI (Body Mass Index)")
print ("<<<<<====================>>>>>")

berat_badan = int(input("Masukan Berat Badan Anda (KG) :")) 
tinggi_badan = float(input("Masukan Tinggi Badan Anda (M) :"))

bmi = berat_badan / (tinggi_badan ** 2)

print("BMI Anda adalah:", round(bmi, 2))

if bmi < 18.5 :
    print("Anda Kekurangan Berat Badan.")
elif bmi >= 18.5 and bmi < 25.0 :
    print("Berat Badan Anda Normal")
elif bmi >= 25.0 and bmi < 30.0 :
    print("Anda Kelebihan Berat Badan")
else:
    print("Berat Badan Anda Obesitas")