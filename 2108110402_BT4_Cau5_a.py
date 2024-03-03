def tim_nguoi_co_so_dien_thoai_ket_thuc_bang_7(user_data):
    ket_qua = []
    for nguoi in user_data:
        so_dien_thoai = nguoi.get("phone", "")
        if so_dien_thoai.endswith("7"):
            ket_qua.append(nguoi)
    return ket_qua

user_data = [
    {"name": "Tuan", "phone": "555-1414", "email": "abc@gmail.com"},
    {"name": "Hung", "phone": "555-1617", "email": "python@gmail.com"},
    {"name": "Trung", "phone": "555-3141", "email": ""},
    {"name": "Hoang", "phone": "555-2717", "email": "laptrinh@gmail.com"},
]

ket_qua_a = tim_nguoi_co_so_dien_thoai_ket_thuc_bang_7(user_data)

print("Những người có số điện thoại kết thúc bằng số 7:")
for nguoi in ket_qua_a:
    print(f"{nguoi['name']} - {nguoi['phone']}")

