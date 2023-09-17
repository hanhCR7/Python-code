import sys
run = True
while run:
    try:
        name = input("Mời nhập tên: ")
        age = int(input("Mời nhập tuổi: "))
        gender = input("Mời nhập giới tính: ")
        experience = int(input("Mời nhập số năm kinh nghiệm trong ngành dịch vụ: "))
        height = float(input("Mời nhập chiều cao (m): "))
        weight = float(input("Mời nhập cân nặng (kg): "))
        if age == 0:
            raise ValueError("Bạn không thể nhập tuổi bằng 0.")
        elif experience == 0:
            raise ValueError("Bạn không thể nhập số năm kinh nghiệm bằng 0.")
        elif height:
            raise ValueError("Bạn không thể nhập chiều cao bằng 0.")
        elif weight == 0:
            raise ValueError("Bạn không thể nhập cân nặng bằng 0.")
        if 30 <= age <= 40:
            if experience >= 5 and height >= 1.55 and weight <= 45:
                print('Chúc mừng bạn đã trúng tuyển!')
            if experience >= 2 and height >= 1.6 and weight >= 50:
                print("Chúc mừng bạn đã trúng tuyển!")
            else:
                print("Chúc mừng bạn đã xịt!")
        elif 18 <= age <= 30:
            if height >= 1.6 and weight <= 50:
                print("Chúc mừng bạn đã trúng tuyển!")
            else:
                print("Chúc mừng bạn đã xịt!")
        else:
            print("Chúc mừng bạn đã xịt!")
    except ValueError as e:
        print(f"Lỗi ValueError: {e}")
    tiepTuc = input("Bấm 't' để tiếp tục, bấm 'k' để dừng: ")
    run = True if tiepTuc == 't' else False

print("Chương trình kết thúc")