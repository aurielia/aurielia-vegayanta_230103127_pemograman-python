def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung ongkos kirim berdasarkan berat, kota, dan asuransi.
    """
    
    if kota == "Surakarta":
        tarif_dasar = 5000
    elif kota == "Jakarta":
        tarif_dasar = 10000
    elif kota == "Bandung":
        tarif_dasar = 8000
    else:
        tarif_dasar = 7000  
    
    total = tarif_dasar + (2000 * berat_kg)
    
    if asuransi:
        total += 3000
    
    return total

print("=== HASIL 1 ===")
print("hitung_ongkir(2, 'Surakarta')")
hasil1 = hitung_ongkir(2, "Surakarta")
print(f"Hasil: Rp {hasil1:,}")
print(f"→ Pengiriman 2 kg ke Surakarta tanpa asuransi")
print()

print("=== HASIL 2 ===")
print("hitung_ongkir(5, 'Jakarta', asuransi=True)")
hasil2 = hitung_ongkir(5, "Jakarta", asuransi=True)
print(f"Hasil: Rp {hasil2:,}")
print(f"→ Pengiriman 5 kg ke Jakarta dengan asuransi")