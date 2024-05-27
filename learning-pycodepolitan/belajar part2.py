# BELAJAR IF-STATEMENT

orang = 100
zombie = 80
if orang < zombie:
    print("Dunia tidak terselamatkan")
if orang > zombie:
    print("Dunia masih bisa diselamatkan")
if orang == zombie:
    print("Siap perang")


# BELAJAR ELSE-STATEMENT

# menggunakan statement If
menang = False
if menang == True:
    print("Selamat!")
if menang == False:
    print("Silakan coba lagi!")

# menggunakan statement Else
menang = False 
if menang == True:
    print("Selamat!")
else:
    print("Silakan coba lagi!")


# BELAJAR ELIF-STATEMENT

# menggunakan statement If dan Else
cowo_anime = input("silakan pilih cowo anime favorit Anda : ")
if cowo_anime == "Ishigami Senku":
    print("Anda memilih cowo anime berkepribadian INTP")
if cowo_anime == "Kiyotaka Ayanokouji":
    print("Anda memilih cowo anime berkepribadian INTJ")
if cowo_anime == "Johan Liebert":
    print("Anda memilih cowo anime berkepribadian INFJ")
else:
    print("Maaf, cowo anime Anda tidak ada di list")

# menggunakan statement Elif
cowo_anime = input("silakan pilih cowo anime favorit Anda : ")
if cowo_anime == "Ishigami Senku":
    print("Anda memilih cowo anime berkepribadian INTP")
elif cowo_anime == "Kiyotaka Ayanokouji":
    print("Anda memilih cowo anime berkepribadian INTJ")
elif cowo_anime == "Johan Liebert":
    print("Anda memilih cowo anime berkepribadian INFJ")
else:
    print("Maaf, cowo anime Anda tidak ada di list")