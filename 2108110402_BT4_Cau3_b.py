lst = [10, 7, 6, 9, 12, 4, 5, 2, 15]
lst_1 = list(filter(lambda x: x%2 == 1, lst))
lst_2 = list(map(lambda x: x*2,lst_1))

print("Danh sach cac so le trong (lst_1):",lst_1)
print("Danh sach cac so le sau khi nhan voi 2 (lst_2):",lst_2)
print("Danh sach cac so le sau khi nhan voi 2 (lst_2):",lst_2)