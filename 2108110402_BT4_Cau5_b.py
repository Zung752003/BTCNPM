def tim_nguoi_khong_co_dia_chi_email(user_data):
    ket_qua = []
    for nguoi in user_data:
        dia_chi_email = nguoi.get("email", "")
        if not dia_chi_email:
            ket_qua.append(nguoi)
    return ket_qua

user_data = [
    {"name": "Tuan", "phone": "555-1414", "email": "abc@gmail.com"},
    {"name": "Hung", "phone": "555-1617", "email": "python@gmail.com"},
    {"name": "Trung", "phone": "555-3141", "email": ""},
    {"name": "Hoang", "phone": "555-2717", "email": "laptrinh@gmail.com"},
]

ket_qua_b = tim_nguoi_khong_co_dia_chi_email(user_data)

print("Những người không có địa chỉ email:")
for nguoi in ket_qua_b:
    print(f"{nguoi['name']} - {nguoi['phone']}")
