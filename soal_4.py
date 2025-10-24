def jadwal_hari(hari):
    """
    Menampilkan jadwal kuliah berdasarkan hari.
    
    Pencarian dilakukan dengan mengecek satu per satu isi list dictionary
    untuk menemukan jadwal yang sesuai dengan hari yang diminta.
    """
    jadwal = [
        {"hari": "Senin", "mata_kuliah": "Pemrograman Python", "waktu": "08:00-10:00"},
        {"hari": "Senin", "mata_kuliah": "Basis Data", "waktu": "10:00-12:00"},
        {"hari": "Selasa", "mata_kuliah": "Jaringan Komputer", "waktu": "13:00-15:00"},
        {"hari": "Rabu", "mata_kuliah": "Algoritma", "waktu": "09:00-11:00"},
        {"hari": "Kamis", "mata_kuliah": "Sistem Operasi", "waktu": "14:00-16:00"},
        {"hari": "Jumat", "mata_kuliah": "Matematika Diskrit", "waktu": "10:00-12:00"}
    ]
    
    hasil = []
    for item in jadwal:
        if item["hari"].lower() == hari.lower():
            hasil.append(item)
    
    return hasil

# Contoh penggunaan
print(jadwal_hari("Selasa"))