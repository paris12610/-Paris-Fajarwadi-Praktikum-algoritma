while True:
    print("\n--- Program Cek Jumlah Hari ---")
    bulan = int(input("Masukkan bulan (1-12): "))
    tahun = int(input("Masukkan tahun: "))

    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        jumlah_hari = 31
    elif bulan in [4, 6, 9, 11]:
        jumlah_hari = 30
    elif bulan == 2:
        # Cek tahun kabisat
        if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
            jumlah_hari = 29
        else:
            jumlah_hari = 28
    else:
        print("Bulan tidak valid! Masukkan angka antara 1 sampai 12.")
        continue

    print(f"Jumlah hari pada bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.")

    ulang = input("\nApakah ingin mencoba lagi? (y/t): ").lower()
    if ulang != 'y':
        print("Program selesai. Terima kasih!")
        break