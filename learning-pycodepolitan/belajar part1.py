# Mulai
print("Mulai")

# Membaca umur
umur = int(input("Masukkan umur Anda: "))

# Membaca tinggi badan
tinggi_badan = int(input("Masukkan tinggi badan Anda (cm): "))

# Apakah umur lebih dari sama dengan 17?
if umur >= 17:
    # Jika iya, apakah tinggi badan lebih dari sama dengan 160?
    if tinggi_badan >= 160:
        # Jika iya, maka output akan mencetak "sudah bisa daftar"
        print("Anda sudah bisa daftar")
    else:
        # Jika tidak, maka output akan mencetak "belum bisa daftar"
        print("Anda belum bisa daftar")
else:
    # Jika umur kurang dari 17, output akan mencetak "belum bisa daftar"
    print("Anda belum bisa daftar")

# Selesai
print("Selesai")