#Program Soal 4 Minggu 11-1
#Ali Ahmad Fahrezy
#187221042

#nb:  Array nama bulan
#i:   Looping counter
#ib:  Nilai bulan dalam integer
#stg: Nilai tanggal dalam string
#sb:  Input nama bulan dalam string
#sth: Nilai tahun dalam string
#sib: Nilai bulan dalam string
#sp:  Nilai bilangan total dalam string
#sr:  Nilai kebalikan dalam string

def main():

    print("Soal Nomor 4 Minggu 11 \"Tanggal Palindrome\"")

    nb = ["januari", "februari", "maret", "april", "mei", "juni", "juli", "agustus", "september", "oktober", "november", "desember"]

    ib = 0
    sr = ""
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

    # Konversi String ke dalam bentuk kebalikannya
    sp = stg + sib + sth
    sr = ""
    for i in range(len(sp) - 1, -1, -1):
        sr = sr + sp[i]

    print("Asli: " + sp)
    print("Reverse: " + sr)
    if (sp == sr):
        print("PALINDROME")
    else:
        print("BUKAN PALINDROME")

if __name__ == "__main__":
    main()