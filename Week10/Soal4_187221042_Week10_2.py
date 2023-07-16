
#Program Soal 4 Minggu 10-1
#Ali Ahmad Fahrezy
#187220142

#j  Input jam
#m  Input menit
#sj Sudut yang terbentuk terhadap garis tegak lurus dan jarum jam
#sm Sudut yang terbentuk terhadap garis tegak lurus dan jarum menit
#sa Sudut yang terbentuk terhadap jarum jam dan jarum menit

def main():

    print("Soal Nomor 4 Minggu 10 \"Menghitung sudut antara jarum jam dan jarum menit\"")

    j = int(input("Inputlah nilai jam: "))
    m = int(input("Inputlah nilai menit: "))

    #Karena dalam menit ada 60 posisi terhadap satu lingkaran 360. Maka perbandingan sudut dengan menit adalah 360/60=6. Maka setiap menit, 6 derajat berpindah.
    sm = m * 6

    #Karena dalam jam ada 12 posisi terhadap satu lingkaran 360. Maka perbandingan sudut dengan jam adalah 360/12=30. Maka setiap menit, 30 derajat berpindah.
    sj = (j + (m / 60)) * 30

    #Besaran sudut jam terhadap menit adalah nilai mutlak pengurangan sudut jam terhadap garis tegak lurus dan menit terhadap garis tegak lurus
    sa = abs(sj - sm)

    #Jika sudut lebih besar daripada 180, maka harus dihitung dari belakang, jadi 360 dikurang dengan sudut akhir
    if sa > 180:
        sa = 360 - sa

    print("Sudut antara jarum jam dan jarum menit adalah " + str(sa) + " derajat")

if __name__ == "__main__":
    main()