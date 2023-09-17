import sys
run = True

while run:
    try:
        keo = int(input("Mời nhập số kẹo: "))
        hocSinh = int(input("Mời nhập số học sinh: "))
        soKeoMoiHS = int(keo / hocSinh)
        keoThua = keo % hocSinh
        print("Số kẹo mỗi học sinh nhận được là: ",soKeoMoiHS)
        print("Số kẹo còn thừa là: ",keoThua)
    except ZeroDivisionError:
        print("Có lỗi exception", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        print("Bạn đã nhập số học sinh là 0 nên chương trình không thực được")
    except ValueError:
        print("Có lỗi exception", sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2])
        print("Bạn cần nhập số !!!!!!!!!!!")
    tiepTuc = input("Bấm 'c' để tiếp tục, bấm 'k' để dừng: ")
    run = True if tiepTuc == 'c' else False

print("Chương trình kết thúc")