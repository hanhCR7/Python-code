class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def calculate_gpa(self):
        if not self.scores:
            return 0

        total_credit = 0
        total_grade_points = 0

        for score in self.scores:
            credit, grade = score
            total_credit += credit
            total_grade_points += credit * grade

        return total_grade_points / total_credit
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("Danh sách học sinh:")
        for student in self.students:
            print(f"Tên: {student.name}")
            print(f"Tuổi: {student.age}")
            print(f"Mã số học sinh: {student.id}")

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Học sinh {student.name} đã được xóa khỏi danh sách.")
        else:
            print("Không tìm thấy học sinh trong danh sách.")

    def calculate_class_gpa(self):
        if not self.students:
            return 0

        total_gpa = 0
        total_students = len(self.students)

        for student in self.students:
            total_gpa += student.calculate_gpa()

        return total_gpa / total_students

def main():
    classroom = Classroom()

    while True:
        print("\n--- Quản lý thông tin học sinh ---")
        print("1. Thêm học sinh")
        print("2. Hiển thị danh sách học sinh")
        print("3. Tìm kiếm học sinh")
        print("4. Xóa học sinh")
        print("5. Nhập diểm")
        print("6. Thoát")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            name = input("Nhập tên học sinh: ")
            age = int(input("Nhập tuổi học sinh: "))
            id = input("Nhập mã số học sinh: ")
            student = Student(name, age, id)
            classroom.add_student(student)
            print("Học sinh đã được thêm vào danh sách.")

        elif choice == '2':
            classroom.display_students()

        elif choice == '3':
            name = input("Nhập tên học sinh cần tìm: ")
            student = classroom.find_student(name)
            if student:
                print(f"Tên: {student.name}")
                print(f"Tuổi: {student.age}")
                print(f"Mã số học sinh: {student.id}")
            else:
                print("Không tìm thấy học sinh trong danh sách.")

        elif choice == '4':
            name = input("Nhập tên học sinh cần xóa: ")
            student = classroom.find_student(name)
            if student:
                classroom.remove_student(student)
            else:
                print("Không tìm thấy học sinh trong danh sách.")
        elif choice == '5':
            name = input("Nhập điểm ")

        elif choice == '6':
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
