def main():
    x = []

    a = 0

    #Proses input array X
    while (a != 5):
        x.append(int(input("Input nilai ke " + str(a + 1) + " untuk array X: ")))
        a = a + 1;
    a = 0

    #Proses sortir
    while (a != 5):
        
        #Karena hanya x[4] yang tidak terurut, maka kita akan mencek setiap nilai dalam array dengan x[4].
        if (x[a] > x[4]):

            #Jika nilai x[i] lebih kecil daripada x[4], maka akan terjadi penukaran nilai hingga array telah tersortir
            temp = x[a]
            x[a] = x[4]
            x[4] = temp
        a = a + 1
    a = 0;
        
    print("Array yang sudah berhasil diurut adalah: ", end = "")
    while (a != 4):
        print(str(x[a]) + ", ", end = "")
        a = a + 1
    print(x[4])

if __name__ == '__main__':
    main()