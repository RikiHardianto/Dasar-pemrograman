def tampilkan_menu():
    print("===== Menu Manajemen Data Mahasiswa =====")
    print("1. Menambahkan Data Mahasiswa")
    print("2. Menampilkan Semua Data Mahasiswa")
    print("3. Mencari Data Mahasiswa Berdasarkan NIM")
    print("4. Menghapus Data Mahasiswa berdasarkan NIM")
    print("5. Keluar")

def tambah_mahasiswa(data):
    nim = input("Masukkan NIM: ")
    if nim in data:
        print("NIM sudah terdaftar!")
        return
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    try:
        ipk = float(input("Masukkan IPK: "))
    except ValueError:
        print("IPK harus berupa angka.")
        return
    data[nim] = {"Nama": nama, "Jurusan": jurusan, "IPK": ipk}
    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_semua(data):
    if not data:
        print("Tidak ada data mahasiswa.")
        return
    print("===== Data Mahasiswa =====")
    for nim, info in data.items():
        print(f"NIM     : {nim}")
        print(f"Nama    : {info['Nama']}")
        print(f"Jurusan : {info['Jurusan']}")
        print(f"IPK     : {info['IPK']}")
        print("----------------------------")

def cari_mahasiswa(data):
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in data:
        info = data[nim]
        print(f"Data Mahasiswa NIM {nim}:")
        print(f"Nama    : {info['Nama']}")
        print(f"Jurusan : {info['Jurusan']}")
        print(f"IPK     : {info['IPK']}")
    else:
        print("Data mahasiswa tidak ditemukan.")

def hapus_mahasiswa(data):
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in data:
        del data[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")


data_mahasiswa = {}

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        tambah_mahasiswa(data_mahasiswa)
    elif pilihan == "2":
        tampilkan_semua(data_mahasiswa)
    elif pilihan == "3":
        cari_mahasiswa(data_mahasiswa)
    elif pilihan == "4":
        hapus_mahasiswa(data_mahasiswa)
    elif pilihan == "5":
        print("Terima kasih! Program sudah selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 sampai 5.")
