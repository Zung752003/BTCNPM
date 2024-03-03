def loc_so_chia_het(lst):
    ket_qua = []
    for so in lst:
        if so % 2 == 0 and so % 3 == 0:
            ket_qua.append(so)
    return ket_qua

lst = [10, 7, 6, 9, 12, 4, 5, 2, 15]
ket_qua_loc = loc_so_chia_het(lst)

print("Các số trong danh sách chia hết cho cả 2 và 3 là:")
for so in ket_qua_loc:
    print(so)

