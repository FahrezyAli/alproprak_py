#Program Soal 2 Minggu 9-1
#Ali Ahmad Fahrezy
#187220142
#
#n  : Input rerata deret
#k  : Nilai k dari deret {6, 9, 11, k}

def main():

    print("Soal Nomor 2 Minggu 9 \"Nilai k dari deret {6, 9, 11, k)\"")

    #Input n
    n = int(input("Input rerata deret (Harus lebih dari 6): "))

    #Menghitung k
    k = ((6+9+11) - (n*4))*(-1)

    #Output
    print("Nilai k adalah: " + str(k))

if __name__ == "__main__":
    main()