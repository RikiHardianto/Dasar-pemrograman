username = input("Masukan Username Anda :")
password = input("Masukan PAssword Anda :")

if username == "admin" and password == "admin123":
    print("Selamat Anda Berhasil Login  Dengan Akses Admin")
elif username == "user" and password == "user123":
    print("Selamat Anda Berhasil Login Dengan Akses terbatas")
elif username == "guest" and password == "" :
    print("Selamat Anda Berhasil Login Dengan Akses minimal")
else :
    print("Akses Di Tolak")