name = input("Mời nhập tên: ")
age = int(input("Mời nhập tuổi: "))
gender = input("Mời nhập giới tính: ")
experience = int(input("Mời nhập số năm kinh nghiệm trong ngành dịch vụ: "))
height = float(input("Mời nhập chiều cao (m): "))
weight = float(input("Mời nhập cân nặng (kg): "))

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









