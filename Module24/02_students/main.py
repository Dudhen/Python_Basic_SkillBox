class Student:

    def __init__(self, sname_and_fname, group, rating):
        self.sname_and_fname = sname_and_fname
        self.group = group
        self.rating = rating


student_1 = Student("Дудченко Арсений", "5", [3, 5, 4, 5, 4])
student_2 = Student("Сальников Владислав", "5", [3, 3, 4, 3, 4])
student_3 = Student("Холодилов Станислав", "5", [4, 5, 4, 4, 4])
student_4 = Student("Шибеко Егор", "5", [3, 5, 3, 4, 3])
student_5 = Student("Гиндич Юрий", "3", [3, 3, 3, 4, 3])
student_6 = Student("Сирко Арсений", "3", [3, 3, 4, 3, 3])
student_7 = Student("Никитин Никита", "3", [4, 5, 5, 5, 4])
student_8 = Student("Негляд Людмила", "1", [5, 5, 5, 5, 4])
student_9 = Student("Батков Дарья", "1", [4, 3, 4, 3, 3])
student_10 = Student("Гронский Богдан", "1", [3, 4, 4, 5, 4])

students = [
    student_1, student_2,
    student_3, student_4,
    student_5, student_6,
    student_7, student_8,
    student_9, student_10
]

result = []

while students:
    student = []
    i = 5
    for i_student in students:
        if sum(i_student.rating) / len(i_student.rating) < i:
            i = sum(i_student.rating) / len(i_student.rating)
            student.clear()
            student.append(i_student)
    result.append(student[0])
    students.remove(student[0])

print("\nРейтинг студентов по возрастанию среднего балла:\n")

for i_student in result:
    print("ФИ: {}. Группа: {}. Средний балл: {}.".format(i_student.sname_and_fname,
                                                         i_student.group,
                                                         sum(i_student.rating) / len(i_student.rating))
          )

# зачтено
