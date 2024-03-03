def loc_so_le (lst):
    ket_qua = []
    for so in lst:
        if so % 2 == 1:
            ket_qua.append(so)
    return (ket_qua)
lst = [10, 7, 6, 9, 12, 4, 5, 2, 15]
lst_1 = loc_so_le(lst)
lst_2 = [ so *2  for so in lst_1]

print("Danh sach so le (lst_1):",lst_1)
print("Danh sach so le nhan voi 2 (lst_2):",lst_2)