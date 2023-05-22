from typing import List;

def main():
        
    n = int(input("Input ukuran array yang diinginkan: "))

    x = []

    #Proses input array
    for i in range(n):
        x.append(int(input("Input data ke " + str(i + 1) + ":  ")))


    #Output
    print("Array yang telah dikurangi dengan nilai terkecil adalah: " + str(kurangNilaiMin(x, n)))


def kurangNilaiMin(x: List[int], n: int):

    #Kita ambil data pertama sebagai nilai maksimum sementara
    m = x[0]

    r = []

    #Looping dimulai dari satu karena index 0 sudah diambil sebagai nilai m sementara
    for i in range(n):

        if (x[i] < m):

            #Jika nilai x[i] lebih rendah daripada nilai m saat ini, maka nilai m = x[i]
            m = x[i]

    for i in range(n):

        #Outputkan nilai array dikurangi dengan nilai terendah
        r.append(x[i] - m)
    
    return r
        
if __name__ == "__main__":
    main()
