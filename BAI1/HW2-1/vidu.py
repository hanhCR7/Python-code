import sys

run = True

while run:
    try:
        diemToan = float(input("Mời nhập điểm toán: "))
        diemVan = float(input("Mời nhập điểm văn: "))
        diemTA = float(input("Mời nhập điểm tiếng anh: "))
        dtb = (diemToan + diemVan + diemTA) / 3
        print("Điểm trung bình cảu bạn là: ", dtb)
        if diemToan == 0 or diemVan == 0 or diemTA == 0:
            raise ValueError("Số điểm không thể bằng 0.")
        if dtb < 4:
            print("Điểm cảu bạn dưới trung bình! Vui lòng ở lớp")
        elif dtb > 4 and dtb <6:
            print("Điểm của bạn ở mức trung bình! Vui lòng học tốt hơn")
        elif dtb > 6 and dtb < 8:
            print("Điểm của bạn ở mức khá! Vui lòng học tốt hơn")
        elif dtb > 8 and dtb < 10:
            print("Điểm của bạn ở mức giỏi! Chúa mừng bạn và hy vọng bạn giữ được phong độ")
        else:
            print("Bạn quá xuất sắc!!!!!!!!!!!!!!")
    except ValueError as e:
        print(f"Lỗi ValueError: {e}")
    tiepTuc = input("Bấm 't' để tiếp tục, bấm 'k' để dừng: ")
    run = True if tiepTuc == 't' else False

print("Chương trình kết thúc")
