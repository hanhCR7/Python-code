def count_mark(grades):
    if not grades:
        return 0, 0

    total_students = len(grades)


    retake_students = sum(1 for grade in grades if grade < 5.0)

    return retake_students, total_students


grades = [6.5, 4.0, 7.8, 3.2, 8.9, 5.5, 2.7]
retake, total = count_mark(grades)
print(f"Số sinh viên học lại: {retake}")
print(f"Tổng số sinh viên trong lớp: {total}")
