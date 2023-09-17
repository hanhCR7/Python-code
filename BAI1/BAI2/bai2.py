import sys

run = True

while run:
    try:
        diemToan = float(input("Mời nhập điểm toán: "))
        diemVan = float(input("Mời nhập điểm văn: "))
        diemTA = float(input("Mời nhập điểm tiếng anh: "))
        dtb = (diemToan + diemVan + diemTA) / 3
        if dtb < 4:
            print("Điểm của bạn dưới trung bình! Vui lòng ở lớp")
        elif 4 <= dtb < 6:
            print("Điểm của bạn ở mức trung bình! Vui lòng học tốt hơn")
        elif 6 <= dtb < 8:
            print("Điểm của bạn ở mức khá! Vui lòng học tốt hơn")
        elif 8 <= dtb <= 10:
            print("Điểm của bạn ở mức giỏi! Chúc mừng bạn và hy vọng bạn duy trì được thành tích")
        else:
            print("Bạn quá xuất sắc!!!!!!!!!!!!!!")
    except ZeroDivisionError:
        print("Lỗi ZeroDivisionError: Bạn đã nhập số điểm là 0 nên chương trình không thể thực hiện được")
    except ValueError:
        print("Lỗi ValueError: Bạn cần nhập số !!!!!!!!!!!")
    tiepTuc = input("Nhấn 't' để tiếp tục, nhấn 'k' để dừng: ")
    if tiepTuc != 't':
        run = False

print("Chương trình kết thúc")
