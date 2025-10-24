import os
import csv
import json
import logging

def setup_logging():
    """Setup logging sederhana"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def create_data_folder():
    """Membuat folder data jika belum ada"""
    try:
        os.makedirs('data', exist_ok=True)
        logging.info("Folder 'data' berhasil dibuat atau sudah ada")
    except Exception as e:
        logging.error(f"Gagal membuat folder 'data': {e}")
        raise

def write_csv_file():
    """Menulis file CSV dengan data presensi"""
    data_presensi = [
        {'nim': '1234567890', 'nama': 'Wijaya', 'hadir_uts': 1},
        {'nim': '1234567891', 'nama': 'Budi', 'hadir_uts': 0},
        {'nim': '1234567892', 'nama': 'Lestari', 'hadir_uts': 1},
        {'nim': '1234567893', 'nama': 'Dian', 'hadir_uts': 1},
        {'nim': '1234567894', 'nama': 'Prasetyo', 'hadir_uts': 0}
    ]
    
    try:
        with open('data/presensi.csv', 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['nim', 'nama', 'hadir_uts']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for data in data_presensi:
                writer.writerow(data)
        
        logging.info("File CSV 'data/presensi.csv' berhasil ditulis")
        
    except Exception as e:
        logging.error(f"Gagal menulis file CSV: {e}")
        raise

def read_csv_and_calculate():
    """Membaca file CSV dan menghitung statistik presensi"""
    try:
        with open('data/presensi.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        logging.info("File CSV 'data/presensi.csv' berhasil dibaca")
        
        # Hitung statistik
        total_mahasiswa = len(data)
        hadir_uts = sum(1 for row in data if row['hadir_uts'] == '1')
        tidak_hadir = total_mahasiswa - hadir_uts
        persentase_hadir = (hadir_uts / total_mahasiswa) * 100 if total_mahasiswa > 0 else 0
        
        # Data untuk JSON
        ringkasan = {
            'total_mahasiswa': total_mahasiswa,
            'hadir_uts': hadir_uts,
            'tidak_hadir': tidak_hadir,
            'persentase_hadir': round(persentase_hadir, 2)
        }
        
        return ringkasan
        
    except FileNotFoundError:
        logging.error("File 'data/presensi.csv' tidak ditemukan")
        raise
    except Exception as e:
        logging.error(f"Gagal membaca file CSV: {e}")
        raise

def write_json_file(ringkasan):
    """Menulis file JSON dengan ringkasan presensi"""
    try:
        with open('data/ringkasan.json', 'w', encoding='utf-8') as file:
            json.dump(ringkasan, file, indent=4, ensure_ascii=False)
        
        logging.info("File JSON 'data/ringkasan.json' berhasil ditulis")
        
    except Exception as e:
        logging.error(f"Gagal menulis file JSON: {e}")
        raise

def main():
    """Fungsi utama untuk menjalankan seluruh proses"""
    logging.info("Memulai proses rekap presensi UTS")
    
    try:
        # 1. Membuat folder data
        create_data_folder()
        
        # 2. Menulis file CSV
        write_csv_file()
        
        # 3. Membaca CSV dan menghitung statistik
        ringkasan = read_csv_and_calculate()
        
        # Menampilkan ringkasan di console
        print("\n=== RINGKASAN PRESENSI UTS ===")
        print(f"Total Mahasiswa: {ringkasan['total_mahasiswa']}")
        print(f"Hadir UTS: {ringkasan['hadir_uts']}")
        print(f"Tidak Hadir: {ringkasan['tidak_hadir']}")
        print(f"Persentase Hadir: {ringkasan['persentase_hadir']}%")
        
        # 4. Menulis file JSON
        write_json_file(ringkasan)
        
        logging.info("Proses rekap presensi UTS berhasil diselesaikan")
        print("\nProses selesai! File tersimpan di folder 'data/'")
        
    except Exception as e:
        logging.error(f"Proses gagal: {e}")
        print(f"\nTerjadi kesalahan: {e}")

if __name__ == "__main__":
    setup_logging()
    main()