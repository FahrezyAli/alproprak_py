#Program Soal 2 Week 14-1
#Ali Ahmad Fahrezy
#187221042
#
#n: Nilai input

def main():
    
    print("Soal Nomor 2 Minggu 14 \"Konversi Integer ke Binari\"")

    n = int(input("Input nilai integer yang ingin diubah ke dalam binari: "))

    print("Binari dari nilai integer tersebut adalah: " + convertBin(n))

#Fungsi untuk konversi nilai integer ke string binari
#
#n: Nilai input
#
#Other Parameters:
#b: String binari
#
#return String binari dari input

def convertBin(n: int):
        
    b = 0

    if (n < 0):
        return "Harus angka positif"
    
    elif (n == 0):
        return "0"
    
    else:

        #Fungsi rekursif dengan cara memanggil kembali convertBin(n / 2), dan digabung dengan n % 2. Ini menggunakan rumus konversi desimal ke binari yaitu membagi 2 angka yang ingin dikonversi, dan jika ia habis maka nilai nya 0, dan jika tidak habis maka nilai nya 1, kemudian dilanjutkan dengan nilai n / 2 dan seterusnya sampai n bernilai 0
        b = convertBin(int(n / 2))
        b += n % 2

    return b

if __name__ == "__main__":
    main()