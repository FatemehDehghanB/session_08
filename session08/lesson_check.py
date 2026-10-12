lesson_list = [
    {"name": "math", 'unit': 2, "teacher": "ali"},
    {"name": "chemistry", 'unit': 3, "teacher": "mohsen"},
    {"name": "geo", 'unit': 5, "teacher": "ehsan"}
]
new_lesson_list = [
    {"name": "math", 'unit': 2, "teacher": "ali"},
    {"name": "biology", 'unit': 2, "teacher": "reza"},
    {"name": "geo", 'unit': 5, "teacher": "ehsan"}
]


def check_in_list(lesson):
    if lesson in lesson_list:
        return lesson


student_list = list(filter(None, (map(check_in_list, new_lesson_list))))


def add_total(lesson):
    if lesson["unit"] == 2:
        price = 1000
    elif lesson["unit"] == 3:
        price = 1200
    elif lesson["unit"] == 5:
        price = 1400
    else:
        price = 0
    lesson["total"] = lesson["unit"] * price
    return lesson


student_list = list(map(add_total, student_list))
print(student_list)
