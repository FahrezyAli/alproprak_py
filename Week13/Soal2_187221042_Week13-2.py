from typing import List

def main():
        
    n = int(input("Input ukuran array yang diinginkan: "))

    x = []

    #Proses input array
    for i in range(n):
        x.append(int(input("Input data ke " + str(i + 1) + ": ")))

    #Output
    print("Frekuensi terbesar dari array tersebut adalah: " + str(maxFreq(x, n)))

def maxFreq(x: List[int], n: int):
        
    c = 1
    f = 0
    
    for i in range(n - 1):

        for j in range(i + 1, n):
                
            #Dilakukan dua looping untuk melihat apakah value dari x[i] sama dengan x[j]
            if (x[i] == x[j]):

                #Jika nilai x[i] sama dengan x[j], maka counter (c) akan bertambah, kemudian nilai x[i] akan dihapus agar tidak terhitung dua kali saat nilai i berubah
                c = c + 1
                x[j] = 0

        if (c > f):

            #Jika nilai counter lebih tinggi daripada frekuensi, maka frekuensi akan diisi dengan nilai counter. Dengan ini, nilai frekuensi terbesar akan pasti didapat dan nilai modus (v) pasti benar
            f = c

        #Counter direset kembali menjadi 1
        c = 1

    return f

if __name__ == "__main__":
    main()