def geserString(s, geserKiri, geserKanan):

    result_kiri = s[geserKiri:] + s[:geserKiri]
    print(result_kiri)
    result_kanan = result_kiri[-(geserKanan):] + result_kiri[:-(geserKanan)]
    print(result_kanan)

    return result_kanan

# Driver program
if __name__ == "__main__":
    s = input("Masukan angka yang ingin digeser: ")
    l = int(input("Masukan jumlah geser kekiri: "))
    r = int(input("Masukan jumlah geser kekanan: "))

    result = geserString(s, l, r)

    print(result)