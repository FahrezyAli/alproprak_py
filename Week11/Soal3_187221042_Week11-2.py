
#Soal 3 Minggu 11-1
#Ali Ahmad Fahrezy
#187221042

#n: Ukuran array
#i: Looping
#e: Index akhir dari deret naik berkelanjutan terpanjang
#x: Array input
#s: Array index awal dari deret naik berkelanjutan
#l: Panjang dari deret naik berkelanjutan
#c: Boolean dari pertanyaan "Apakah awal deret berhasil ditemukan"

def main():
    print("Soal Nomor 3 Minggu 11 \"LCIS\"")

    n = int(input("Input ukuran array: "))

    x = []

    #Proses input nilai array x
    for i in range(n):
        x.append(int(input("Input nilai ke " + str(i + 1) + ": ")))

    #Memberikan nilai 0 pada s dan l agar tidak error
    s = []
    l = []

    for i in range(2):
        s.append(0)
        l.append(0)

    c = False
    
    for i in range(n):
        if (i == 0):
            #Jika i = 0, maka deret baru saja dimulai sehingga panjang deret (l[0]) adalah 1
            l[0] = 1
        elif (x[i] >= x[i - 1]):
            if not(c):
                #Karena c masih false, maka deret baru saja dimulai sehingga awal index (s[0]) bisa diambil dan c diubah menjadi true untuk menandakan bahwa awal index telah ditemukan
                s[0] = i - 1
                c = True
            #Jika nilai x[i] lebih kecil daripada nilai sebelumya (x[i - 1]), maka panjang dari deret (l[0]) bertambah 1
            l[0] = l[0] + 1
        else:
            #Jika deret naik berkelanjutan sudah selesai (nilai x[i] tidak lebih besar daripada nilai x[i - 1]), maka panjang deret (l[0])pun di kembalikan lagi menjadi 1 agar dapat menghitung panjang deret yang lain jika ada
            l[0] = 1

            #Kondisi c diubah menjadi false karena deret naik berkelanjutan sudah selesai
            c = False
        #Setiap langkah dari loop, jika panjang deret yang sedang berlangsung (l[0]) lebih besar daripada panjang deret sebelumnya, maka nilai panjang terbesar akan disimpan di l[1] beserta dengan awal indexnya (s[1])
        if (l[0] > l[1]):
            l[1] = l[0]
            s[1] = s[0]

    #Untuk mendapatkan index akhir dari deret naik berkelanjutan, kita dapat menghitungnya dengan menjumlahkan nilai awal index(s[1]) dengan panjang deret (l[1]), kemudian dikurangi satu karena index array dimulai dari 0
    e = s[1] + l[1] - 1

    #Proses output
    
    print("Array bilangan ascending berurutan terpanjang: ", end = "")
    if (l[1] == 1):
        print("Tidak ada")
    else:
        for i in range(s[1], e + 1):
            print(str(x[i]), end = " ")
        print("(" + str(l[1]) + ")")

if __name__ == "__main__":
    main()