def geserString(s, geserKiri, geserKanan):
    # slice string in two parts for left and right
    Lfirst = s[0: geserKiri]
    Lsecond = s[geserKiri:]
    result_kiri = Lsecond + Lfirst
    Rfirst = result_kiri[0: len(s) - geserKanan]
    Rsecond = result_kiri[len(s) - geserKanan:]
    result_kanan = Rsecond + Rfirst

    print("Lfirst", Lfirst)
    print("Lsecond", Lsecond)
    print("Rfirst", Rfirst)
    print("Rsecond", Rsecond)
    print("Left Rotation : ", result_kiri)
    print("Right Rotation : ", result_kanan)

    return result_kanan

# Driver program
if __name__ == "__main__":
    s = input("Masukan angka yang ingin digeser: ")
    l = int(input("Masukan jumlah geser kekiri: "))
    r = int(input("Masukan jumlah geser kekanan: "))

    result = geserString(s, l, r)
    print(result)