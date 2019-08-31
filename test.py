def BubbleSort(val):
    for passnum in range(len(val) - 1, 0, -1):
        for i in range(passnum):
            if val[i] > val[i + 1]:
                temp = val[i]
                val[i] = val[i + 1]
                val[i + 1] = temp


DaftarAngka = [23, 7, 32, 99, 4, 15, 11, 20]
BubbleSort(DaftarAngka)
print(DaftarAngka)


def SelectionSort(val):
    for isi in range(len(val) - 1, 0, -1):
        Max = 0
        for lokasi in range(1, isi + 1):
            if val[lokasi] > val[Max]:
                Max = lokasi

        temp = val[isi]
        val[isi] = val[Max]
        val[Max] = temp


DaftarAngka = [23, 7, 32, 99, 4, 15, 11, 20]
SelectionSort(DaftarAngka)
print(DaftarAngka)


def InsertionSort(val):
    for index in range(1, len(val)):

        valueaktif = val[index]
        posisi = index

        while posisi > 0 and val[posisi - 1] > valueaktif:
            val[posisi] = val[posisi - 1]
            posisi = posisi - 1

        val[posisi] = valueaktif


DaftarAngka = [23, 7, 32, 99, 4, 15, 11, 20]
InsertionSort(DaftarAngka)
print(DaftarAngka)