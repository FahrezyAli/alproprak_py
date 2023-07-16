from Soal5_187221042_Week14_2 import numFactor

from typing import List

#Program Soal 6 Minggu 14-1
#Ali Ahmad Fahrezy
#187221042
#
#n: Nilai input

def main():
    
    print("Soal Nomor 6 Minggu 14 \"List Faktor Prima Suatu Integer\"")

    n = int(input("Input nilai integer yang ingin dicari faktor prima nya: "))

    print("Faktor prima dari nilai integer tersebut adalah: " + str(disp_prime_factor(n, 1, [])))

#Fungsi untuk mendapatkan faktor prima dari suatu integer
#
#n: Input
#i: Looping
#r: List rekursif
#
#return List faktor prima

def disp_prime_factor(n: int, i: int, r: List[int]) -> List[int]:
    
    if (i <= n / 2):
        if (n % i == 0 and numFactor(i, 1) == 2):
            
            #Jika i merupakan faktor dari n dan i merupakan bilangan prima (numFactor == 2). Maka nilai i akan di output
            r.append(i)

        #Rekursif dengan menambahkan nilai i + 1 untuk mencoba nilai i lainnya
        disp_prime_factor(n, i + 1, r)

    else:
        if (numFactor(n, 1) == 2):
            r.append(n)

    return r

if __name__ == "__main__":
    main()
