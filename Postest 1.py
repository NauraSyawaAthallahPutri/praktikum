#Login
print("=============Login==============")
nama = input("Masukkan nama anda:")
kelas = input("Masukkan kelas anda:")

#Untuk mengecek apakah nim dan pin yang dimasukkan merupakan integers
while True:
    try:
        nim = int(input("Masukkan NIM anda:"))
        pin = int(input("Masukkan PIN anda: "))
        break #berhenti looping jika input yang dimasukkan berupa integers
    except ValueError:
        print("Tidak valid")

#Func untuk menampilkan ouput dari input di atas
def login():
    print(f"Halo, {nama} dengan NIM {nim} dari kelas {kelas}. Anda berhasil Login!")
login()

# Pilihan Operasi
print("==============Pilihan volume bangun ruang=================")
print("1. Bola")
print("2. Tabung")
print("3. Limas segitiga")

#Untuk mengecek apakah variabel pilih yang dimasukkan merupakan angka
while True:
    try:
        pilih = int(input("Pilih bangun ruang yang ingin anda hitung volumenya (m):") )
        if pilih > 0 and pilih < 4: 
            break #berhenti looping jika input yang dimasukkan berupa integers dan 0 < pilih <4
        else:
            print("Angka yang diinput antara 1 sampai 3")
    except ValueError:
        print("Mohon masukkan angka")

#Operasi untuk bola dan tabung
if pilih == 1 or pilih == 2:
    tinggi = float(input("Masukkan tinggi: "))
    r = float(input("Masukkan jari-jari:"))
    if r % 7 == 0:
        phi = 22/7
    else:
        phi = 3.14

    #Menghitung volume bola
    if pilih == 1:
        bangun_ruang = "bola"
        hasil = (4/3) * phi * (r**3)
    #Menghitung volume tabung
    else:
        bangun_ruang = "tabung"
        hasil = phi* (r**2) *tinggi

#Menghitung volume limas segtiga
if pilih == 3:
    bangun_ruang = "limas segitiga"
    alas_segitiga = float(input("Masukkan alas segitiga:"))
    tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))
    tinggi = float(input("Masukkan tinggi limas: "))
    
    luas_alas = 1/2 * alas_segitiga * tinggi_segitiga
    hasil = 1/3 * luas_alas * tinggi

#Ouput akhir
print(f"Volume dari {bangun_ruang} tersebut adalah {hasil} m³")