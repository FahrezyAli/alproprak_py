#Program Soal 4 Minggu 14-1
#Ali Ahmad Fahrezy
#187221042
#
#n: Nilai input

def main():
    
    print("Soal Nomor 4 Minggu 14 \"Jumlah dari Faktor Suatu Integer\"")

    n = int(input("Input nilai integer yang ingin dicari jumlah dari nilai faktornya: "))

    print("Jumlah dari nilai faktor dari nilai integer tersebut adalah: " + str(sumFactor(n, 1)))

#Fungsi untuk menghitung jumlah dari semua faktor faktor dari suatu integer
#
#n: Input
#i: Looping
#   
#Other Parameters:
#sum: Jumlah faktor faktor
#
#return Jumlah faktor faktor
    
def sumFactor(n: int, i: int):

    _sum = 0

    #n / 2 karena nilai faktor tertinggi selain nilai itu sendiri adalah nilai n / 2
    if (i <= n / 2):

        #Rekursif dengan menambahkan nilai i + 1 untuk mencoba nilai i lainnya
        _sum = sumFactor(n, i + 1)
        if (n % i == 0):
            #Jika nilai i dapat membagi habis n, maka nilai i akan ditambahkan ke sum
            _sum = _sum + i

    else:
        _sum = n
    
    return _sum

if __name__ == "__main__":
    main()
