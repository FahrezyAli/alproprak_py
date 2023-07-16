#Program Soal 5 Minggu 14-1
#Ali Ahmad Fahrezy
#187221042
#
#n: Nilai input

def main():

    print("Soal Nomor 5 Minggu 14 \"Total Faktor dari Suatu Integer\"")

    n = int(input("Input nilai integer yang ingin dicari jumlah faktornya: "))

    print("Total faktor dari nilai integer tersebut adalah: " + str(num_factor(n, 1)))

#Fungsi untuk menghitung total faktor dari suatu integer
#
#n: Input
#i: Looping
#
#Other Parameters:
#t: Total faktor
#
#return Total faktor
    
def num_factor(n: int, i: int) -> int:
        
    t = 0

    #n / 2 karena nilai faktor tertinggi selain nilai itu sendiri adalah nilai n / 2
    if (i <= n / 2):
        
        #Rekursif dengan menambahkan nilai i + 1 untuk mencoba nilai i lainnya
        t = num_factor(n, i + 1)
        if (n % i == 0):
            #Jika nilai i dapat membagi habis n, maka nilai i akan ditambahkan ke sum
            t = t + 1

    else:
        t = 1

    return t

if __name__ == "__main__":
    main()
