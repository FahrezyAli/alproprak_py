def main():
    
    print("Soal Nomor 4 Minggu 13 \"Rotasi array\"")

    print("Soal Nomor 3 Minggu 13 \"Median Array\"")

    n = int(input(("Input ukuran array yang diinginkan: ")))

    x = []

    #Proses input array
    for i in range(n):
        x.append(int(input("Input data ke " + str(i + 1) + ": ")))

    #Output
    print("Median dari array tersebut adalah: " + str(median(x, n)))

def median(x, n):

    #Lokasi median adalah panjang data (n) dibagi 2. Namun, karena index array dimulai dari 0, maka nilai n harus dikurangi dengan 1 terlebih dahulu
    m = 0

    l = int((n - 1) / 2)

    #Melihat apakah panjang array ganjil / genap
    if (n % 2 == 0):

        #Jika n adalah genap, maka nilai median adalah nilai tengah dari dua nilai yang berada ditengah, dalam hal ini adalah x[i] dan nilai setelahnya x[i + 1], kemudian dibagi dua
        m = (x[l] + x[l + 1]) / 2
    
    else:

        #Jika n adalah ganjil, maka nilai median adalah nilai pada lokasi l
        m = x[l]

    return m

if __name__ == "__main__":
    main()
