from typing import List

def main():
        
    n = int(input("Input ukuran array yang diinginkan: "))

    x = []

    #Proses input array
    for i in range(n):
    
        x.append(int(input("Input data ke " + str(i + 1) + ": ")))

    #Input jumlah langkah rotasi
    r = int(input("Input berapa langkah rotasi: "))

    while (r > n):
        r = int(input("Langkah tidak boleh lebih besar daripada ukuran array: "))

    #Input arah rotasi
    d = int(input("Input arah rotasi. 1 untuk kanan dan -1 untuk kiri: "))

    while (d != 1 and d != -1):
        d = int(input("Arah harus bernilai 1 atau -1: "))

    #Output
    s = ""
    if (d == 1):
        s = "kanan"
    else:
        s = "kiri"

    print("Hasil rotasi " + str(r) + " langkah ke " + s + " adalah: " + str(rotate(x, n, r, d)))

def rotate(x: List[int], n: int, r: int, d: int) -> List[int]:
        
    f = 0
    t = 0

    result = []

    #Metode ini menggunakan index dua lapis (two layer index)
    if (d == 1):

        f = n - r
        t = n * 2 - r
    
    else:
        f = r
        t = n + r
        
    for i in range(f, t):

        if (i >= n):
            
            #Nilai index layer 2 tersebut di kurangi dengan nilai n untuk mengkonversi kembali ke nilai index layer 1
            result.append(x[i - n])
        
        else:
            result.append(x[i])
            
    return result

if __name__ == "__main__":
    main()
