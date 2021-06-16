# Задача с пункта 8.
# Вместо строк в списке друзей должны быть такие же словари как джон и марта.
# Создайте по 2 друга для джона и марты.
# Выведите в консоль поля Джона и Марты.

vanya = {
    'Full_name': "Vanya",
    'Age': 17,
    'Salary': 1320.5,
    'Gender': True,
    'Friends': ["John", "Sanya", "Vitalya"],
    'Coordinates': (50.447254, 30.5212699)
}
sanya = {
    'Full_name': "Sanya",
    'Age': 28,
    'Salary': 1870.5,
    'Gender': True,
    'Friends': ["John", "Vanya", "Vitalya"],
    'Coordinates': (50.447254, 30.5212699)
}
john = {
    'Full_name': "John",
    'Age': 25,
    'Salary': 1500.5,
    'Gender': True,
    'Friends': [vanya['Full_name'], sanya['Full_name']],
    'Coordinates': (50.447254, 30.5212699)
}

sveta = {
    'Full_name': "Marta",
    'Age': 48,
    'Salary': 2000.1,
    'Gender': False,
    'Friends': ["Marta", "Nedenka", "Taniusha"],
    'Coordinates': (52.412331, 28.5235325)
}
nadya = {
    'Full_name': "Marta",
    'Age': 48,
    'Salary': 2000.1,
    'Gender': False,
    'Friends': ["Svetik", "Marta", "Taniusha"],
    'Coordinates': (52.412331, 28.5235325)
}
marta = {
    'Full_name': "Marta",
    'Age': 48,
    'Salary': 2000.1,
    'Gender': False,
    'Friends': [sveta['Full_name'], nadya['Full_name']],
    'Coordinates': (52.412331, 28.5235325)
}

for key, value in john.items():
    print(f"{key}  => {value}")
print("------------------------")
for key, value in marta.items():
    print(f"{key}  => {value}")
