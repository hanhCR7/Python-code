from datetime import datetime
class Person:
    def __init__(self, name, birthdate, address, phone):
        self.name = name
        self.birthdate = birthdate
        self.address = address
        self.phone = phone
    def nhap(self):
        self.name = input("Nhập tên: ")
        self.birthdate = input("Nhập ngày sinh (YYYY-MM-DD): ")
        self.address = input("Nhập địa chỉ: ")
        self.phone = input("Nhập số điện thoại: ")
        self.birthdate = datetime.strptime(self.birthdate, "%Y-%m-%d")
    def get_age(self):
        today = datetime.now()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age
    def print_info(self):
        print("----------THÔNG TIN NGƯỜI NHẬP----------")
        print(f"Họ và tên: {self.name}")
        print(f"Ngày, tháng, năm sinh: {self.birthdate.strftime('%Y-%m-%d')}")
        print(f"Địa chỉ: {self.address}")
        print(f"Số điện thoại: {self.phone}")

def main():
    person1 = Person("", "", "", "")
    person1.nhap()
    person1.print_info()
    age = person1.get_age()
    print(f"Tuổi: {age}")

if __name__ == "__main__":
    main()