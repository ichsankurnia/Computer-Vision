# mutia = [1,2,3,4,10,11] # list
mutia = []  # list

jumlah_index = int(input("Masukan jumlah index: "))

for i in range(jumlah_index):
    index = int(input("masukan isi: "))
    mutia.append(index)

print(mutia)


# print(mutia)
# total = mutia[0]+mutia[1]+mutia[2]+mutia[3]+mutia[4]+mutia[5]
# print()

total = 0
for i in mutia:
    # print(i)
    total = total + i

print(total)