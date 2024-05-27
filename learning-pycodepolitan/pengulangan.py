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