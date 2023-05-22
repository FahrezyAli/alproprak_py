import math

#Soal 1 Minggu 10-2
#Ali Ahmad Fahrezy
#187220142

#x1 Titik lokasi x lingkaran pertama
#y1 Titik lokasi y lingkaran pertama
#r1 Jari-jari lingkaran pertama
#x2 Titik lokasi x lingkaran kedua
#y2 Titik lokasi y lingkaran kedua
#r2 Jari-jari lingkaran kedua
#rb Jari-jari lingkaran terbesar
#rk Jari-jari lingkaran terkecil
#a  Alas atau jarak titik pusat dua lingkaran di sumbu x
#t  Tinggi atau jarak titik pusat lingkaran di sumbu y
#d  Jarak titik pusat dua lingkaran

def main():    
    x1 = float(input("Inputlah nilai sumbu x titik pusat lingkaran pertama: "))
    y1 = float(input("Inputlah nilai sumbu y titik pusat lingkaran pertama: "))
    r1 = float(input("Inputlah jari-jari lingkaran pertama: "))

    x2 = float(input("Inputlah nilai sumbu x titik pusat lingkaran kedua: "))
    y2 = float(input("Inputlah nilai sumbu y titik pusat lingkaran kedua: "))
    r2 = float(input("Inputlah jari-jari lingkaran pertama: "))

    #Menghitung nilai jarak alas atau jarak antara x1 dan x2
    a = abs(x1 - x2)

    #Menghitung nilai tinggi atau jarak antara y1 dan y2
    t = abs(y1 - y2)

    #Menghitung jarak antara kedua lingkaran dengan menggunakan teorama pythagoras
    d = math.sqrt((a * a) + (t * t))

    #Mengambil nilai jari-jari terbesar antara kedua lingkaran
    rb = max(r1, r2)

    #Mengambil nilai jari-jari terkecil antara kedua lingkaran
    rk = min(r1, r2)

    #Posisi dasar adalah P1, yaitu sama sekali tidak menyentuh
    h = "P1"

    #Jika nilai jarak adalah sama dengan penjumlahan kedua jari jari lingkaran, maka terbukti bahwa lingkaran tersebut saling bersinggungan di luar (P2)
    if d == rb + rk:
        h = "P2"

    #Jika nilai jarak adalah sama dengan pengurangan jari jari terbesar dengan yang terkecil, maka terbukti bahwa lingkaran tersebut saling bersinggungan di dalam (P3)
    if rb - rk < d and d < rb + rk:
        h = "P3"

    #Jika nilai pengurangan jari jari terbesar dengan jari jari terkecil adalah lebih kecil dari pada jarak, dan nilai jarak adalah lebih kecil dari pada nilai penjumlahan kedua jari jari, maka terbukti terbentuk arsiran ditengah kedua lingkaran, dimana terdapat dua titik potong antara dua lingkaran (P3)
    if d == rb - rk:
        h = "P4"

    #Jika nilai penjumlahan jarak dan jari jari terkecil adalah lebih kecil dari pada nilai jari jari terbesar, maka terbukti bahwa lingkaran terkecil tersebut berada didalam lingkaran terbesar tanpa bersinggungan (P5)
    if (d + rk < rb):
        h = "P5"

    print("Posisi kedua lingkaran tersebut adalah: " + h)

if __name__ == "__main__":
    main()