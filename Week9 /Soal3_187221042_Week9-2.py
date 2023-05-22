#Soal 3 Minggu 9-1
#Ali Ahmad Fahrezy
#187220142
#b  : Harga beli
#pb : Persentase beli
#u  : Keuntungan
#o  : Ongkos kirim
#h  : Pertambahan harga
#pj : Persentase pertambahan harga

def main():
    #Input harga  beli
    b = int(input("Input harga beli: "))

    #Input persentase pembelian
    pb = int(input("Input persentase pembelian (Harus antara 1-100): "))

    #Input nilai keuntungan
    u = int(input("Input keuntungan yang diinginkan: "))

    #Menghitung ongkos kirim
    o = b*pb/100

    #Menghitung pertambahan harga
    h = o + u

    #Menghitung persentase pertambahan harga
    pj = h/b*100

    #Output
    print("Persentase pertambahan harga: " + str(pj) + "%");

if __name__ == "__main__":
    main()