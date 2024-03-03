lst = [10, 7, 6, 9, 12, 4, 5, 2, 15]
ket_qua_loc = list(filter(lambda x: x%2 == 0 and x%3 ==0, lst))
print("Cac so trong danh sach chi het cho 2 va 3 la:")
for so in ket_qua_loc:
    print(so)

