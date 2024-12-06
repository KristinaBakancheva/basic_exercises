from collections import defaultdict, Counter

# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Петя"},
]
items_students = defaultdict(int)
for student in students:
    items_students[student.get("first_name")] += 1
for key, val in items_students.items():
    print(f"{key}: {val}")

#или можно так. А что лучше?
first_names = [x["first_name"] for x in students] 
items_students = Counter(first_names)
for key, val in items_students.items():
    print(f"{key}: {val}")


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
def most_often_object(objects):
    often_object = str()
    often_id = 0
    for key, val in objects.items():
        if often_id == 0 or often_id<val:
            often_object = key
            often_id = val
    return often_object

students = [
    {"first_name": "Вася"},
    {"first_name": "Петя"},
    {"first_name": "Маша"},
    {"first_name": "Маша"},
    {"first_name": "Оля"},
]

first_names = [x["first_name"] for x in students] 
items_students = Counter(first_names)
print(most_often_object(items_students))
# не учетена ситуация, что может быть несколько имен у которых максимальное использование. 
# Что б это учесть можем просто добавить проверку на добавление имя в set если у них val одинаковые



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {"first_name": "Вася"},
        {"first_name": "Вася"},
    ],
    [  # это – второй класс
        {"first_name": "Маша"},
        {"first_name": "Маша"},
        {"first_name": "Оля"},
    ],[  # это – третий класс
        {"first_name": "Женя"},
        {"first_name": "Петя"},
        {"first_name": "Женя"},
        {"first_name": "Саша"},
    ],
]
for count, value in enumerate(school_students):
    first_names = [x.get("first_name") for x in value] 
    items_students = Counter(first_names)
    print(f"Самое частое имя в классе {count+1}: {most_often_object(items_students)}")


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "2б", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
    {"class": "2в", "students": [{"first_name": "Даша"}, {"first_name": "Олег"}, {"first_name": "Маша"}]},
]
is_male = {
    "Олег": True,
    "Маша": False,
    "Оля": False,
    "Миша": True,
    "Даша": False,
}
def items_gender(students, male):
    item = 0
    for student in students:
        if is_male.get(student) == male:
            item += 1
    return item

for classes in school:
    num_class = classes.get("class")
    list_students = [x.get("first_name") for x in classes.get("students")]
    girls = items_gender(list_students, False)
    boys = items_gender(list_students, True)
    print(f"Класс {num_class}: девочки {girls}, мальчики {boys} ") 
    #вопрос, получается кавычки в кавычках с f строкой только одинарные? Экранирование не работает и даже перенос нормально


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {"class": "2a", "students": [{"first_name": "Маша"}, {"first_name": "Оля"}]},
    {"class": "3c", "students": [{"first_name": "Олег"}, {"first_name": "Миша"}]},
]
is_male = {
    "Маша": False,
    "Оля": False,
    "Олег": True,
    "Миша": True,
}
items_girls = dict()
items_boys = dict()

for classes in school:
    num_class = classes.get("class")
    list_students = [x.get("first_name") for x in classes.get("students")]
    items_girls[num_class] = items_gender(list_students, False)
    items_boys[num_class] = items_gender(list_students, True)
class_girl = most_often_object(items_girls)
class_boy = most_often_object(items_boys)

print(f"Больше всего мальчиков в классе {class_boy}")
print(f"Больше всего девочек в классе {class_girl}")


