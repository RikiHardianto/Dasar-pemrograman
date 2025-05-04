daftar_belanja = []

print("Masukkan 5 item belanjaan :")
for i in range (5) :
    item = input(f"item ke {i+1}:")
    daftar_belanja.append(item)
    
print("Daftar belanja Anda:")
for i, item in enumerate(daftar_belanja, start=1) :
    print(f"{i}.{item}")
    
item_dihapus = input("Masukkan nama item yang sudah Di beli dan ingin di hapus :")
    
if item_dihapus in daftar_belanja :
    daftar_belanja.remove(item_dihapus)
    print(f"Item ",item_dihapus,"Telah di hapus dari daftar.")
else:
    print(f"item",item_dihapus,"Tidak ada di dalam daftar.")
    
print("Daftar belanja yng sudah di perbarui :")
for i , item in enumerate (daftar_belanja, start = 1) :
    print(f"{i}.{item}")