#Soal 1 Minggu 11-1
#Ali Ahmad Fahrezy
#187221042

#b:    Array berat 10 bebek
#m:    Mean berat 10 bebek
#s:    Selisih berat antara 2 bebek yang hilang
#j:    Jumlah berat antara 2 bebek yang hilang
#sum:  Jumlah berat 8 bebek yang masih ada
#svar: Variabel bantu untuk menghitung variance
#var:  Variance
#i:    Looping

def main():

    print("Soal Nomor 1 Minggu 11 \"Berat Bebek\"")

    _sum = 0
    svar = 0

    b = []
    for i in range(8):
        b.append(int(input("Inputlah berat bebek ke " + str(i + 1) + ": ")))
        _sum = _sum + b[i]
    
    m = float(input("Inputlah mean dari berat 10 bebek: "))
    s = float(input("Inputlah selisih antara 2 bebek yang hilang: "))

    #Dengan menggukanan rumus mean sebagai dasar. Dibentuk rumus yang digunakan untuk mencari jumlah 2 berat bebek yang hilang
    j = -_sum + m * 10

    #Kemudian kita dapat menggunakan substitusi dengan jumlah dan selisih 2 bebek yang hilang untuk menemukan berat masing masing bebek tersebut
    b.append((j - s) / 2)
    b.append(s + b[8])

    #Berat bebek yang sudah lengkap kemudian dioutput, sekaligus menghitung svar
    for i in range(10):
        print("Berat bebek ke " + str(i + 1) + " adalah " + str(b[i]))
        svar = svar + (b[i] - m) * (b[i] - m)

    #Menghitung variance, dan kemudian dioutput
    var = svar / 10
    print("Variance 10 bebek adalah: " + str(var))
    
if __name__ == "__main__":
    main()