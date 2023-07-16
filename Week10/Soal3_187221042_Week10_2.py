#Program Soal 3 Minggu 10-2
#Ali Ahmad Fahrezy
#187220142

#a  Nilai a
#b  Nilai b
#c  Nilai c
#d  Nilai d
#e  Nilai e
#b2 Nilai b parabola terhadap garis
#c2 Nilai c parabola terhadap garis
#ds Diskriminan
#x1 Titik potong X1
#y1 Titik potong Y1
#x2 Titik potong X2
#y2 Titik potong Y2
#k  Keterangan

import math


def main():

    print("Soal Nomor 3 Minggu 10 \"Melihat hubungan antara parabola dan garis\"")

    a = int(input("Inputlah nilai a: "))
    b = int(input("Inputlah nilai b: "))
    c = int(input("Inputlah nilai c: "))
    d = int(input("Inputlah nilai d: "))
    e = int(input("Inputlah nilai e: "))

    #Menghitung nilai b parabola terhadap garis
    b2 = b - d

    #Menghitung nilai c parabola terhadap garis
    c2 = c - e

    #Menghitung diskriminan parabola terhadap garis
    ds = (b2 * b2) - (4 * a * c2)

    k = ""

    #Jika D < 0, maka parabola dan garis saling lepas
    if ds < 0:
        k = "Saling Lepas"
    else:
        #jika D = 0. maka parabola dan garis bersinggungan
        if ds == 0:
            k = "Bersinggungan"
        else:
            #jika D < 0, maka parabola dan garis berpotongan
            k = "Berpotongan"

        #Menghitung posisi x1 dengan rumus abc
        x1 = ((-b2) - math.sqrt(ds))
        x1 = x1/2*a

        #Menghitung posisi x2 dengan rumus abc
        x2 = ((-b2) + math.sqrt(ds))
        x2 = x2/2*a

        #Menghitung posisi y1 dengan memasukkan nilai x1 ke fungsi linear
        y1 = (d*x1+e)

        #Menghitung posisi y2 dengan memasukkan nilai x2 ke fungsi linear
        y2 = (d*x2+e)

        print("Posisi X1 =  " + str(x1) + "\nPosisi Y1 = " + str(y1) + "\nPosisi X2 =  " + str(x2) + "\nPosisi Y2 = " + str(y2))

    print("Keterangan: " + k)

if __name__ == "__main__":
    main()