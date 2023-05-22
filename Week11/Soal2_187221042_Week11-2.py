#Soal 2 Minggu 11-1
#Ali Ahmad Fahrezy
#187221042

#b: Array berat 10 bebek
#i: Looping
#k: Total status kurus
#l: Total status langsing
#s: Total status Standard
#g: Total status gemuk
#o: Total status obesitas

def main():
    b = []

    k = 0
    l = 0
    s = 0
    g = 0
    o = 0

    #Kode ini berfungsi untuk looping input berat 10 bebek dalam satuan kilogram
    for i in range(10):
        b.append(float(input("Inputlah berat bebek ke " + str(i + 1) + " dengan satuan kilogram: ")))

    #Kemudian masing masing berat akan dicek apakah status-nya kurus, langsing, standard, gemuk atau obesitas, yang kemudian akan menambah total count dari status tersebut
    for i in range(10):
        if (b[i] < 0.7):
            k = k + 1
        elif (b[i] < 1):
            l = l + 1
        elif (b[i] < 1.5):
            s = s + 1
        elif (b[i] < 2):
            g = g + 1
        else:
            o = o + 1

    #Status tersebut kemudian di output
    print("Bebek yang memiliki status KURUS: " + str(k))
    print("Bebek yang memiliki status LANGSING: " + str(l))
    print("Bebek yang memiliki status STANDARD: " + str(s))
    print("Bebek yang memiliki status GEMUK: " + str(g))
    print("Bebek yang memiliki status OBESITAS: " + str(o))

if __name__ == "__main__":
    main()
