def main():
    s = input("Input kalimat yang ingin di cek apakah palindrome atau tidak: ")

    #String r diberi string kosong ("") agar tidak error
    r = ""

    #Dengan membuat looping decreasing dari nilai index akhir string ke awal string, kita dapat membalikkan (reverse) suatu string
    i = len(s) - 1
    while (i >= 0):
        r = r + s[i]
        i = i - 1

    #Proses output
    print("Status: ", end = "")
    if (s == r):
        print("PALINDROME")
    else:
        print("BUKAN PALINDROME")

if __name__ == "__main__":
    main()