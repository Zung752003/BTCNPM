def tinh_tong(n):
    if n < 1:
        return "Vui lòng nhập một số nguyên dương lớn hơn hoặc bằng 1."
    
    total = sum(range(1, n + 1))
    return f"Tổng của các số từ 1 đến {n} là: {total}"

# Nhập giá trị n từ bàn phím
try:
    n = int(input("Nhập giá trị n: "))
    print(tinh_tong(n))
except ValueError:
    print("Vui lòng nhập một số nguyên.")
    