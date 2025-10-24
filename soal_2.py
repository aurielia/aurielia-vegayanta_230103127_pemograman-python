setor1 = int(input("Masukkan setoran minggu 1: "))
setor2 = int(input("Masukkan setoran minggu 2: "))
setor3 = int(input("Masukkan setoran minggu 3: "))

if setor1 < 0 or setor2 < 0 or setor3 < 0:
    print("Input tidak valid!")

else:
    total = setor1 + setor2 + setor3
    print(f"Total Setoran : {total}")

    if total < 300000:
        print   ("rendah")
    elif total < 600000:
        print("sedang")
    else:
        print("tinggi")
