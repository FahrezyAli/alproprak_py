def main():
    
    n = int(input("Input ukuran array: "))
    
    x = []

    #Proses input nilai array x
    i = 0;
    while (i != n):
        x.append(int(input("Input nilai ke " + str(i + 1) + ": ")))
        i = i + 1

    #Memberikan nilai 0 pada s, l dan t agar tidak error
    s = []
    l = []
    t = []

    i = 0
    while (i != 2):
        s.append(0)
        l.append(0)
        t.append(0)
        i = i + 1
        
    c = False
    i = 0
    while (i != n):
        if (i == 0):
            
            #Jika i = 0, maka deret baru saja dimulai sehingga panjang deret (l[0]) adalah 1
            l[0] = 1
        else:
            if (x[i] >= x[i - 1]):
                if (c):
                    
                    #Jika c sudah true, maka awal index tidak diambil lagi agar nilai nya tidak tertimpa dan nilai total terus ditambahkan
                    t[0] = t[0] + x[i]
                else:
                    
                    #Karena c masih false, maka deret baru saja dimulai sehingga awal index (s[0]) bisa diambil dan nilai total dapat mulai dijumlahkan
                    s[0] = i - 1
                    t[0] = x[i - 1] + x[i]
                    c = True

                #Jika nilai x[i] lebih kecil daripada nilai sebelumya (x[i - 1]), maka panjang dari deret (l[0]) bertambah 1
                l[0] = l[0] + 1

            else:
                
                #Jika deret naik berkelanjutan sudah selesai (nilai x[i] tidak lebih besar daripada nilai x[i - 1]), maka panjang deret (l[0])pun di kembalikan lagi menjadi 1 agar dapat menghitung panjang deret yang lain jika ada, dan nilai total (t[0]) diubah kembali menjadi 0 agar dapat menghitung nilai total deret lain jika ada
                l[0] = 1
                t[0] = 0

                #Kondisi c diubah menjadi false karena deret naik berkelanjutan sudah selesai
                c = False

            #Setiap langkah dari loop, jika nilai total deret yang sedang berlangsung (t[0]) lebih besar daripada nilai total deret sebelumnya, maka nilai panjang terbesar akan disimpan di t[1] beserta dengan awal indexnya (s[1]) dan panjang nya (l[1])
            if (t[0] > t[1]):
                l[1] = l[0]
                s[1] = s[0]
                t[1] = t[0]

        i = i + 1

    #Untuk mendapatkan index akhir dari deret naik berkelanjutan, kita dapat menghitungnya dengan menjumlahkan nilai awal index(s[1]) dengan panjang deret (l[1])
    e = s[1] + l[1]

    #Proses output
    print("Array bilangan ascending berurutan terpanjang: ", end = "")
    if (l[1] == 1):
        print("Tidak ada")

    i = s[1]
    while (i != e):
        print(str(x[i]) + " ", end = "")
        i = i + 1
    
    print("(" + str(t[1]) + ")")

if __name__ == "__main__":
    main()