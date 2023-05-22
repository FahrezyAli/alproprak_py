#Soal 4 Minggu 11-1
#Ali Ahmad Fahrezy
#187221042

#nb:  Array nama bulan
#i:   Looping counter
#ib:  Nilai bulan dalam integer
#itg: Nilai tanggal dalam integer
#ip:  Nilai bilangan total dalam integer
#ir:  Nilai kebalikan dalam integer
#n:   Variabel bantu dalam perhitugan reverse
#stg: Nilai tanggal dalam string
#sb:  Input nama bulan dalam string
#sth: Nilai tahun dalam string
#sib: Nilai bulan dalam string
#sp:  Nilai bilangan total dalam string
#sr:  Nilai kebalikan dalam string

def main():
    nb = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]

    ib = 0
    l = 0
    n = 0
    sr = ""

    ir = 0
    sib = ""

    stg = input("Input tanggal: ")
    sb = input("Input bulan: ").lower()
    sth = input("Input tahun: ")

    #Looping ini berfungsi untuk mengkonversi nama bulan menjadi nilai angka bulan tersebut
    for i in range(12):
        if (sb == nb[i]):
            ib = i + 1
            if (ib < 10):
                sib = "0" + str(ib)
            else:
                sib = str(ib)

    #Keseluruhan konversi string to integer, integer to string, dan if itg < 10 ini berfungsi agar nilai tanggal seperti "02, 05, 09" tidak hilang menjadi "2, 5, 9" dikarenakan integer tidak dapat menyimpan nilai "02, 05, 09"
    sp = stg + sib + sth
    ip = int(sp)
    itg = int(stg)
    if (itg > 10):
        l = 7
    else:
        l = 6
    n = ip

    #Kode ini berfungsi untuk membalikkan nilai n dan memasukkannya kedalam variabel ir
    for i in range(l + 1):
        ir = ir * 10 + n % 10
        n = int(n / 10)

    if (itg > 10):
        sr = str(ir)
    else:
        sr = str(ir) + "0"

    print("Asli: " + sp)
    print("Reverse: " + sr)
    if (sp == sr):
        print("PALINDROME")
    else:
        print("BUKAN PALINDROME")

if __name__ == "__main__":
    main()