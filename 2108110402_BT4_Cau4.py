def nhap_danh_sach():
    danh_sach =[]
    for i in range(5):
        try:
            so = int(input(f"nhap so nguyen duong thu{i+1}:" ))
            if so < 0:
                raise ValueError ("Day la so nguyen am, hay nhap lai")
            danh_sach.append(so)
        except ValueError:
            print("Day la ky tu chu, hay nhap lai")
    return danh_sach
danh_sach_so = nhap_danh_sach()
print("Danh sach so nguyen duong da nhap:",danh_sach_so)