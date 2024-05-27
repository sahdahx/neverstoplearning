# BELAJAR MEMBUAT METHOD / FUNCTION

nama = []
def print_nama():
    for data in nama:
        print(data)
    print('==================================')

nama.append("Sahda")
print_nama()

nama.append("Huwaidah")
print_nama()

nama.append("Estiningtyas")
print_nama()

# BELAJAR METHOD PARAMETER

def say_hello(first_name, last_name):
    print(f"Hello {first_name, last_name}")

say_hello("Eko", "Kurniawan")
say_hello("Joko", "Tingkir")

# BELAJAR DEFAULT ARGUMENT VALUE

def jumlahkan(satu, dua, tiga):
    total = satu + dua + tiga
    print(f"Total {[satu, dua, tiga]} = {total}")

jumlahkan(13, 44, 21)


# BELAJAR ARGUMENT LIST

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")
    # BELAJAR RETURN VALUE, tambahkan total untuk mengambil data total
    return (total)

total = jumlahkan(11, 22, 33, 44, 90)

print(total)

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka, total)

list_angka, total = jumlahkan(11, 22, 33, 44, 90)

print(f"Total {list_angka} = {total}")


# BELAJAR TIPE DATA DICTIONARY

print('==================================')

customer = {"Name":"Sahda", "Age":17, "City":"Jogja"}
name = customer["Name"]
age = customer["Age"]
city = customer["City"]

for key, value in customer.items():
    print(f"{key}:{value}")

customer["Company"] = "Badan Pusat Statistik"
customer["Name"] = "Asada Yamazaki"
del customer["City"]

for key, value in customer.items():
    print(f"{key}:{value}")

print('==================================')


# BELAJAR KEYWORD ARGUMENT LIST

def create_html(tag, text):
    html = f"<{tag}>{text}</{tag}>"
    return html

html = create_html("p", "Halo Python")
print(html)
html = create_html("a", "Ini link")
print(html)

def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"
    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "Halo Python")
print(html)
html = create_html("a", "Ini link")
print(html)