# BELAJAR MODULE, belajar cara import file py lain kesini

import function

hello = function.say_hello("Sahda")
print(hello)
hasil = function.total(2,3,4,10)
print(hasil)

# cara menginput satu atau beberapa method kesini, menggunakan from
from function import total

hasil = function.total(1, 2, 3)
print(hasil)

# BELAJAR STRING METHODS
# https://docs.python.org/3.7/library/stdtypes.html#string-methods

nama = "saHda hUwAidAh esTininGtyas"
print(nama)
print(nama.lower())         #huruf kecil semua
print(nama.upper())         #huruf kapital semua
print(nama.capitalize())    #huruf kapital di awal kata pertama
print(nama.title())         #huruf kapital di awal kata
print(nama.split(" "))      #memecah sebuah string menjadi potongan-potongan kecil