student_list = [
    {"name": "Jame",
     "class": "301"},
    {"name": "Jack",
     "class": "302"},
    {"name": "Lucy",
     "class": "303"}
]

for student_info in student_list:
    for student_info_inner in student_info:
        print(student_info[student_info_inner])

