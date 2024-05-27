# BELAJAR LIST

# .append untuk menambahkan data ke dalam list
karakter_anime = ["Nami", "Asada", "Sahda"]
karakter_anime.append("Sachi")
karakter_anime.append("Senku")
print(karakter_anime)

# remove untuk menghapus data di dalam list
karakter_anime.remove("Sahda")
print(karakter_anime)

# [] untuk mencari data urutan ke sekian di list
print(karakter_anime[0])
print(karakter_anime[1])
print(karakter_anime[3])

# len untuk mengecek ukuran list atau berapa banyak data yang ada di list
print(len(karakter_anime))


# BELAJAR FOR-LOOP

# for in untuk mengakses semua data di list
for nama in karakter_anime:
    print('========================')
    print(f"Karakter Anime : {nama}")
    print('========================')


# BELAJAR RANGE

# nomor = [1, 2, 3,... 20]
nomor = range(1, 21)
for no in nomor:
    print(no)


# MEMBUAT PROGRAM MENGGUNAKAN FOR-LOOP, LIST, DAN RANGE

banyak = int(input("Berapa banyak data? "))
nama = []
umur = []

for i in range(0, banyak):
    print(f"Data ke {i}")
    input_nama = input("Nama : ")
    input_umur = int(input("Umur : "))

    nama.append(input_nama)
    umur.append(input_umur)

# code output pertama
print(nama)
print(umur)

#code output kedua
for i in range(0, len(nama)):
    data_nama = nama[i]
    data_umur = umur[i]
    print(f"{data_nama} berumur {data_umur} tahun.")
print('================================================')

# BELAJAR WHILE LOOP

# melakukan perulangan berdasarkan kondisi boolean
# pada while loop, kode akan dieksekusi perulangannya (loop) sampai mendapatkan kondisi true
# loop tidak akan berhenti sampai menemukan kondisi true pada while 
data = ""
while data != "x":
    print("Ulangi lagi!")
    data = input("data : ")

# bisa juga menggunakan untuk break
while True:
    data = input("Data : ")
    if data == "x":
        break
    print(data)

# BELAJAR CONTINUE

# digunakan untuk men-skip proses perulangan di dalam loop
for i in range(1, 50):
    if i % 2 == 0: 
        continue
        print(i)
# bilangan yang dimodulo 2 bersisa 0 akan adalah bilangan genap
# artinya semua bilangan genap akan diskip, sehingga outputnya adalah semua bilangan ganjil dari range 1-50


# BELAJAR BREAK

# digunakan untuk men-stop proses perulangan di dalam loop
for i in range(1, 50):
    if i  / 4 == 5:
        break
    print(i)

print('================================================')

# BELAJAR TUPLE
# mirip dengan list tapi berbeda. Kalau list bisa diubah, kalau tuple tidak bisa.

# list outputnya bisa dijalankan
pelanggan = ["Eko", "Joko", "Andi"]
pelanggan [0] = "Wahyu"
print(pelanggan)

# tuple akan menghasilkan error karena datanya tidak bisa diubah
#pelanggan = ("Eko", "Joko", "Andi")
#pelanggan [0] = "Wahyu"
#print(pelanggan)

# BELAJAR SET
# set tidak bisa memasukkan dua data yang sama, cocok untuk menyimpan data yang unik. Sedangkan list dan tuple bisa.
# set tidak mendukung pengambilan data menggunakan index, hanya menggunakan loop
# set hanya mendukung menambah data (add) atau menghapus data (remove)

# list  -> []
# tuple -> ()
# set   -> {}

nama = {"Eko", "Joko", "Andi", "Eko", "Andi"}
nama.add("Kurniawan")
print(nama)

nama.remove("Andi")
for data in nama:
    print(data)