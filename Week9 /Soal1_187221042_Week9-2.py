#Soal 1 Minggu 9-2
#Ali Ahmad Fahrezy
#187220142
#x      : Input warisan ibu dan satu anak
#ibu    : Jatah warisan ibu
#sisa   : Sisa warisan setelah memisahkan jatah ibu
#anak   : Jatah warisan satu anak
#warisan: Total warisan

def main():

    print("Soal Nomor 1 Minggu 9 \"Warisan\"")

    #Input x
    x = float(input("Input nilai warisan yang diterima ibu dan satu anak: "))

    #Ibu mendapat 1/4 bagian
    ibu = 1/4

    #Sisanya adalah 3/4
    sisa = 1 - ibu

    #Satu anak mendapatkan 1/3 dari sisa tersebut
    anak = 1/3*sisa

    #Kalkulasi warisan
    warisan = x/(ibu + anak)

    #Output
    print("Total warisan: " + str(warisan))

if __name__ == "__main__":
    main()