students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests_and_countLets(dict):
    interests = list()
    countLets = list()
    for i_value in dict.values():
        interests.extend(i_value["interests"])
        countLets.extend(i_value["surname"])
    return interests, len(countLets)


for i_student, i_age in students.items():
    print("Student id:", i_student, ", age:", i_age['age'])

interests, countLets = interests_and_countLets(students)
print("Student interests:", interests, "\nTotal length of all students' surnames:", countLets, "letters.")

# зачтено
