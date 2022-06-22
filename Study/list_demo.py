courses_list = ["Chinese", "Math", "English", "Physics", "Chemistry"]
class_list = ["301", "302", "303"]
courses_list.insert(1, "Biology")
courses_list.extend(class_list)

for courses in courses_list:
    if courses_list.index(courses) <= 5:
        print("This course is %s" % courses)
    else:
        print("The number of this class is %s" % courses)
