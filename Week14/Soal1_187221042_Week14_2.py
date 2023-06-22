#Program Soal 1 Minggu 14-1
#Ali Ahmad Fahrezy
#187221042
#
#n: Nilai input

def main():

    print("Soal Nomor 1 Minggu 14 \"Digit Terbesar dari suatu Integer\"")

    n = int(input("Input nilai integer yang ingin dicari digit terbesar-nya: "))

    print("Digit terbesar dari array tersebut adalah : " + str(max(n)))

#Fungsi untuk mendapatkan nilai digit terbesar dari integer multi digit
#
#n: Nilai input
#
#Other Parameters:
#m: Nilai terbesar (maksimum)
#d: Digit yang telah dipisah dari integer
#
#return Digit terbesar input tersebut
    
def max(n: int) -> int:
    
    m = 0

    #Rumus ini memisah nilai digit paling belakang dari n ke dalam d
    d = n % 10
    if (n > 0):
        #nilai awal m adalah fungsi rekursif max dimana n / 10 untuk menghapus nilai paling belakang yang sudah dimasukkan d
        m = max(int(n / 10))
        if (d > m):
            #JIka d lebih besar dari m, maka m akan diisi dengan d
            m = d

    else:
        m = d

    return m

if __name__ == "__main__":
    main()