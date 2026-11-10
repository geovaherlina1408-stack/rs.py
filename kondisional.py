print("========================================")
print(" PROGRAM PELAYANAN PASIEN RAWAT INAP RS")
print("========================================")

for i in range(1, 11):

    print("\nDATA PASIEN KE-", i)

    nama = input("Nama pasien: ")
    penyakit = input("Jenis penyakit: ")
    lama = int(input("Lama opname (hari): "))

    print("\nPILIH PEMBAYARAN")
    print("1. BPJS")
    print("2. Umum")
    print("3. Asuransi")
    bayar = int(input("Pilihan pembayaran: "))

    print("\nPILIH KELAS KAMAR")
    print("1. VIP")
    print("2. Kelas 1")
    print("3. Kelas 2")
    print("4. Kelas 3")
    kelas = int(input("Pilihan kamar: "))

    # Fasilitas kamar
    if kelas == 1:
        fasilitas = "AC, TV, kulkas, sofa, kamar mandi dalam"
    elif kelas == 2:
        fasilitas = "AC, TV, lemari, kamar mandi"
    elif kelas == 3:
        fasilitas = "Tempat tidur, lemari, fasilitas bersama"
    elif kelas == 4:
        fasilitas = "Tempat tidur dan fasilitas bersama"
    else:
        fasilitas = "Pilihan kamar tidak valid"

    # Pelayanan berdasarkan lama opname
    if lama >= 3:
        pelayanan = "Mendapat fasilitas rawat inap, pemeriksaan rutin, dan pemantauan dokter"
        makanan = "3 kali makan sehari dan 2 kali makanan selingan sesuai diet"
        fasilitas_tambahan = "Perlengkapan mandi, pakaian pasien, dan pemeriksaan berkala"
    else:
        pelayanan = "Mendapat pemeriksaan dan observasi sesuai kondisi pasien"
        makanan = "Menu makanan sesuai kondisi dan jadwal rumah sakit"
        fasilitas_tambahan = "Fasilitas sesuai kebutuhan perawatan"

    # Jadwal kunjungan
    if lama >= 3:
        kunjungan = "10.00-12.00 dan 16.00-18.00"
        aturan = "Maksimal 2 pengunjung secara bergantian"
    else:
        kunjungan = "Mengikuti jadwal kunjungan rumah sakit"
        aturan = "Mengikuti aturan ruang perawatan"

    # Pembayaran
    if bayar == 1:
        pembayaran = "BPJS Kesehatan"
        biaya = "Sesuai ketentuan dan hak kepesertaan BPJS"
    elif bayar == 2:
        pembayaran = "Umum"
        biaya = "Dibayar secara mandiri"
    elif bayar == 3:
        pembayaran = "Asuransi"
        biaya = "Sesuai ketentuan polis asuransi"
    else:
        pembayaran = "Tidak valid"
        biaya = "Pilihan pembayaran tidak tersedia"

    # Hasil
    print("\n========== HASIL PELAYANAN PASIEN ==========")
    print("Nama Pasien       :", nama)
    print("Penyakit          :", penyakit)
    print("Lama Opname       :", lama, "hari")
    print("Pembayaran        :", pembayaran)
    print("Kelas Kamar       :", kelas)
    print("Fasilitas Kamar   :", fasilitas)
    print("Pelayanan         :", pelayanan)
    print("Makanan           :", makanan)
    print("Fasilitas Tambahan:", fasilitas_tambahan)
    print("Jadwal Kunjungan  :", kunjungan)
    print("Aturan Kunjungan  :", aturan)
    print("Keterangan Biaya  :", biaya)
    print("============================================")

print("\n10 PASIEN SELESAI DIPROSES")