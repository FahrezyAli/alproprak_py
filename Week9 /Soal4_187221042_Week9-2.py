#Soal 4 Minggu 9-1
#Ali Ahmad Fahrezy
#187220142
#jo : Jam keberangkatan
#mo : Menit keberangkatan
#td : Total detik waktu keberangkatan
#v  : Kecepatan bus
#s  : Jarak yang ditempuh bus
#w  : Total detik waktu kedatangan
#ja : Jam kedatangan
#ma : Menit kedatangan

def main():

    print("Soal Nomor 4 Minggu 9 \"Waktu Kedatangan Bus\"")

    jo = int(input("Input jam keberangkatan: "))

    mo = int(input("Input menit keberangkatan: "))

    v = int(input("Input kecepatan bus dalam km/jam: "))

    s = int(input("Input jarak yang akan ditempuh dalam km: "))

    #Menghitung total detik waktu keberangkatan
    td = (jo*3600)+(mo*60)

    #Konversi km/jam ke m/s
    v = v*1000/3600

    #Konversi jam ke s
    s = s*1000

    w = s/v+td+2700

    ja = int(w/3600)

    ma = int((w-(3600*ja))/60)

    #Output
    print("Anda akan sampai pada pukul: " + str(ja) + ":" + str(ma))

if __name__ == "__main__":
    main()