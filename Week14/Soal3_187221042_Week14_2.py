from typing import List

#Program Soal 3 Minggu 14-1
#Ali Ahmad Fahrezy
#187221042
#
#n: Nilai input

def main():
    
    print("Soal Nomor 3 Minggu 14 \"List Faktor suatu Integer\"")

    n = int(input("Input nilai integer yang ingin dicari faktornya: "))

    print("Faktor faktor dari nilai integer tersebut adalah: " + str(dispFactor(n, 1 , [])))

#Fungsi untuk mendapatkan faktor faktor dari suatu integer
#
#n: Input
#i: Looping
#r: List rekursif
#
#return List faktor faktor dari suatu integer

def dispFactor(n: int, i: int, r: List[int]):
    
    #n / 2 karena nilai faktor tertinggi selain nilai itu sendiri adalah nilai n / 2
    if (i <= n / 2):
        if (n % i == 0):
            #Jika nilai i dapat membagi habis n, maka nilai i akan dioutput
            r.append(i)

        #Rekursif dengan menambahkan nilai i + 1 untuk mencoba nilai i lainnya
        dispFactor(n, i + 1, r)

    else:
        r.append(n)

    return r

if __name__ == "__main__":
    main()