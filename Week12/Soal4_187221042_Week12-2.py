def main():
    n = int(input("Input ukuran deret Fibonacci: "))

    f = []
    
    f.append(int(input("Input nilai pertama: ")))

    f.append(int(input("Input nilai kedua: ")))

    #Karena nilai f[0] dan f[1] telah diisi pengguna, maka nilai yang akan dicari deret fibonacci nya dimulai dari f[2], menjelaskan mengapa i = 2
    i = 2
    while (i < n):
        
        #Nilai fibonacci f[i] adalah penjumlahan nilai f[i - 1] dan f[i - 2]
        f.append(f[i - 2] + f[i - 1])
        i = i + 1

    #Proses Output
    print("Deret Fibonacci: ", end = "")
    i = 0
    while (i < n - 1):
        print(str(f[i]) + ", ", end = "")
        i = i + 1

    print(f[n - 1])

if __name__ == "__main__":
    main()