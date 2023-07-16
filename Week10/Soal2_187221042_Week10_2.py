#Program Soal 2 Minggu 10-2
#Ali Ahmad Fahrezy
#187220142

#i Input jarak total perjalanan
#w Input waktu perjalanan
#c Input status hujan dalam boolean
#h Total harga perjalanan

def main():

    print("Soal Nomor 2 Minggu 10 \"Menghitung harga transportasi online MyJex\"")

    j = int(input("Inputlah jarak total perjalanan dalam km: "))
    w = int(input("Inputlah waktu total perjalanan dalam menit: "))
    c = input("Input status hujan dengan 'hujan' jika hujan, dan 'cerah' jika cerah: ")

    #Harga dasar perjalanan adalah 10.000
    h = 10000

    #Jika jarak adalah atau lebih dari 3, maka harga akan bertambah 2000 per km tambahan
    if j > 3:
        h = h + ((j - 3) * 2000)

    #Jika waktu per jarak melebihi 2 menit, maka harga akan bertambah 1000 per menit tambahan
    if w / j > 2:
        h = h + ((w % j) * 1000)

    #Jika hujan, maka harga akan bertambah 15%
    if c == "hujan":
        h = (h + (h * 0.15))

    print("Harga total perjalanan: " + str(h))

if __name__ == "__main__":
    main()