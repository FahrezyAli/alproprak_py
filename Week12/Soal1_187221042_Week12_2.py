def main():

    print("Soal Nomor 1 Minggu 12 \"Sortir dua array kedalam satu array\"")

    x = [] 
    y = []
    z = []
    
    a = 0
    
    #Proses input array X
    while (a < 5):
        x.append(int(input("Input nilai ke " + str(a + 1) + " untuk data X: ")))
        z.append(x[a])
        a = a + 1
    a = 0

    #Proses input array Y
    while (a < 5):
        y.append(int(input("Input nilai ke " + str(a + 1) + " untuk data Y: ")))
        z.append(y[a])
        a = a + 1
    a = 0

    #Proses sortir data Z
    while (a < 9):
        b = a + 1
        while (b < 10):
            if (z[a] > z[b]):
                
                #JIka sebuah data z[i] lebih besar daripada seluruh angka sisa dari array (awal sampai akhir), maka, dengan looping ini data tersebut akan dipindahkan hingga sesuai dengan urutan yang benar
                temp = z[a]
                z[a] = z[b]
                z[b] = temp
            b = b + 1
        a = a + 1
    a = 0

    print("Array yang sudah berhasil diurut adalah: ", end = "")
    while (a < 9):
        print(str(z[a]) + ", ", end = "")
        a = a + 1
    print(z[9])

if __name__ == "__main__":
    main()